from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Game class
class Game:
    def __init__(self, name, price, details):
        self.name = name
        self.price = price
        self.details = details

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "details": self.details,
        }

# User class
class User:
    users = {}

    def __init__(self, username, password, email, user_id):
        self._username = username
        self._password = password
        self._email = email
        self._user_id = user_id
        self._purchase_history = {}
        self._credit_card = {}
        self._paypal = {}
        User.users[self._user_id] = self

    def add_game_hs(self, game, price):
        self._purchase_history[game] = price

    def add_credit_card(self, card_name, card_number, expiration, cvv):
        self._credit_card[card_name] = CreditCard(card_number, expiration, cvv)

    def add_paypal(self, email, password):
        self._paypal[email] = Paypal(email, password)

# CreditCard class
class CreditCard:
    def __init__(self, card_number, expiration, cvv):
        self._card_number = card_number
        self._expiration = expiration
        self._cvv = cvv

# PayPal class
class Paypal:
    def __init__(self, email, password):
        self._email = email
        self._password = password

# Cart class
class Cart:
    def __init__(self, user_id):
        self._user_id = user_id
        self._cart = []

    def add_game(self, game):
        self._cart.append(game)
        return {"message": f"Added {game.name} to cart."}

    def remove_game(self, game):
        if game in self._cart:
            self._cart.remove(game)
            return {"message": f"Removed {game.name} from cart."}
        else:
            return {"error": "GameNotFound"}

    def view_cart(self):
        if len(self._cart) == 0:
            return {"message": "Your cart is empty."}
        else:
            games = [{"name": game.name, "price": game.price} for game in self._cart]
            return {"games": games}

    def total_price(self):
        return sum(game.price for game in self._cart)

# Purchase class
class Purchase:
    user_purchase = {}

    def __init__(self, user_id):
        self._user_id = user_id
        Purchase.user_purchase[self._user_id] = self

    def pay_with_credit_card(self, card_name, card_number, expiration, cvv, save_status):
        user = User.users[self._user_id]
        cart = Cart.carts[self._user_id]
        if save_status.lower() == 'yes':
            user.add_credit_card(card_name, card_number, expiration, cvv)
        # Process payment with PayPal
        for gm in cart.games():
            user.add_game_hs(gm._name, gm._price)
        return {f"Paid {cart.total_price()} using Creditcard {card_number}"}

    def pay_with_paypal(self, email, password, save_status):
        user = User.users[self._user_id]
        cart = Cart.carts[self._user_id]
        if save_status.lower() == 'yes':
            user.add_paypal(email, password)
        # Process payment with PayPal
        for gm in cart.games():
            user.add_game_hs(gm._name, gm._price)
        return {f"Paid {cart.total_price()} using PayPal account {email}"}

    def own_card(self, payment_type, card_name):
        user = User.users[self._user_id]
        if payment_type.lower() == 'creditcard' and card_name in user._credit_card:
            pm = user._credit_card[card_name]
            return self.pay_with_credit_card(card_name, pm._card_number, pm._expiration, pm._cvv, 'no')
        elif payment_type.lower() == 'paypal' and card_name in user._paypal:
            pm = user._paypal[card_name]
            return self.pay_with_paypal(pm._email, pm._password, 'no')
        else:
            return {"Payment not found"}

# Game list
games = [
    Game("GTA V", 1850, "Open-world action-adventure game."),
    Game("Minecraft", 790, "Sandbox game where you can build and explore."),
    Game("Fortnite", 0, "A FREE Battle royale game with cartoon graphics."),
    Game("Hogwart", 1500, "Single-player Action-adventure game"),
    Game("Skyrim", 1400, "Single-player Action game"),
    Game("Destiny", 900, "Multi-player FPS game"),
    Game("Fall Guys", 500, "A battle royale game"),
    Game("Among Us", 120, "A multiplayer game where you work together to find the imposter on a spaceship"),
    Game("Valheim", 280, "A Viking-themed survival game where you explore and build in a procedurally generated world"),
    Game("Phasmophobia", 350, "A horror game where you and your team investigate haunted locations and try to capture evidence of ghosts"),
]

# Wishlist class
class Wishlist:
    wishlists = {}

    def __init__(self, user_id):
        self._user_id = user_id
        self._wishlist = []
        Wishlist.wishlists[self._user_id] = self

    def add_game(self, game):
        self._wishlist.append(game)
        return {"message": f"Added {game.name} to wishlist."}

    def remove_game(self, game):
        if game in self._wishlist:
            self._wishlist.remove(game)
            return {"message": f"Removed {game.name} from wishlist."}
        else:
            return {"error": "GameNotFound"}

    def view_wishlist(self):
        if len(self._wishlist) == 0:
            return {"message": "Your wishlist is empty."}
        else:
            games = [{"name": game.name, "price": game.price} for game in self._wishlist]
            return {"games": games}

# FastAPI route handlers
@app.get("/games")
async def get_games():
    game_dicts = [game.to_dict() for game in games]
    return game_dicts

# FastAPI route handlers for wishlist
@app.post("/users/{user_id}/wishlist/add_game")
async def add_game_to_wishlist(user_id: int, game_index: int):
    user = User.users[user_id]
    wishlist = Wishlist(user_id)
    game = games[game_index]
    return wishlist.add_game(game)

@app.post("/users/{user_id}/wishlist/remove_game")
async def remove_game_from_wishlist(user_id: int, game_index: int):
    user = User.users[user_id]
    wishlist = Wishlist(user_id)
    game = games[game_index]
    return wishlist.remove_game(game)

@app.get("/users/{user_id}/wishlist/view_wishlist")
async def view_wishlist(user_id: int):
    user = User.users[user_id]
    wishlist = Wishlist(user_id)
    return wishlist.view_wishlist()

@app.post("/users/{user_id}/cart/add_game")
async def add_game_to_cart(user_id: int, game_index: int):
    user = User.users[user_id]
    cart = Cart(user_id)
    game = games[game_index]
    return cart.add_game(game)

@app.post("/users/{user_id}/cart/remove_game")
async def remove_game_from_cart(user_id: int, game_index: int):
    user = User.users[user_id]
    cart = Cart(user_id)
    game = games[game_index]
    return cart.remove_game(game)

@app.get("/users/{user_id}/cart/view_cart")
async def view_cart(user_id: int):
    user = User.users[user_id]
    cart = Cart(user_id)
    return cart.view_cart()

@app.get("/users/{user_id}/cart/total_price")
async def get_total_price(user_id: int):
    user = User.users[user_id]
    cart = Cart(user_id)
    return {"total_price": cart.total_price()}

# FastAPI route handlers for payment
@app.post("/users/{user_id}/payment/pay_with_credit_card")
async def make_payment_with_credit_card(user_id: int, card_name: str, card_number: str, expiration: str, cvv: str, save_status: str):
    purchase = Purchase(user_id)
    return purchase.pay_with_credit_card(card_name, card_number, expiration, cvv, save_status)

@app.post("/users/{user_id}/payment/pay_with_paypal")
async def make_payment_with_paypal(user_id: int, email: str, password: str, save_status: str):
    purchase = Purchase(user_id)
    return purchase.pay_with_paypal(email, password, save_status)

@app.post("/users/{user_id}/payment/use_own_card")
async def make_payment_with_own_card(user_id: int, payment_type: str, card_name: str):
    purchase = Purchase(user_id)
    return purchase.own_card(payment_type, card_name)