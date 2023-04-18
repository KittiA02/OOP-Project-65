from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Game:
    def __init__(self, name, price):
        self._name = name
        self._price = price
class Cart:
    carts = {}
    def __init__(self,user_id):
        self._cart = []
        self._user_id = user_id
        Cart.carts[self._user_id] = self
    def games(self):
        return self._cart
    def add_game(self, game):
        self._cart.append(game)
        print(f"Added {game._name} to cart.")

    def remove_game(self, game):
        if game in self._cart:
            self._cart.remove(game)
        else:
            print("404 not found")

    def view_cart(self):
        if len(self._cart) == 0:
            print("Your cart is empty.")
        else:
            for game in self._cart:
                print(f"{game._name} - {game._price:.2f} Baht")

    def total_price(self):
        return sum(game._price for game in self._cart)

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
    def add_game_hs(self,game,price):
        self._purchase_history[game] = price
    def add_credit_card(self,card_name,card_number, expiration, cvv):
        self._credit_card[card_name] = CreditCard(card_number, expiration, cvv)
    def add_paypal(self, email, password):
        self._paypal[email] = Paypal(email, password)
    

class Purchase:
    user_purchase = {}
    def __init__(self,user_id):
        self._user_id = user_id
        Purchase.user_purchase[self._user_id] = self
    def pay_with_credit_card(self,card_name,card_number, expiration, cvv, save_status):
        user = User.users[self._user_id]
        cart = Cart.carts[self._user_id]
        if save_status.lower() == 'yes':
            user.add_credit_card(card_name,card_number, expiration, cvv)
        # Process payment with PayPal
        for gm in cart.games():
            user.add_game_hs(gm._name,gm._price)
        return {f"Paid {cart.total_price()} using Creditcard {card_number}"}

    def pay_with_paypal(self,email, password, save_status):
        user = User.users[self._user_id]
        cart = Cart.carts[self._user_id]
        if save_status.lower() == 'yes':
            user.add_paypal(email, password)
        # Process payment with PayPal
        for gm in cart.games():
            user.add_game_hs(gm._name,gm._price)
        return {f"Paid {cart.total_price()} using PayPal account {email}"}

    def own_card(self,payment_type,card_name):
        user = User.users[self._user_id]
        if payment_type.lower() == 'creditcard' and card_name in user._credit_card:
            pm = user._credit_card[card_name]
            return self.pay_with_credit_card(card_name,pm._card_number, pm._expiration, pm._cvv, 'no')
        elif payment_type.lower() == 'paypal' and card_name in user._paypal:
            pm = user._paypal[card_name]
            return self.pay_with_paypal(pm._email, pm._password, 'no')
        else:
            return {"Payment not found"}
class CreditCard:
    def __init__(self, card_number, expiration, cvv):
        self._card_number = card_number
        self._expiration = expiration
        self._cvv = cvv
class Paypal:
    def __init__(self, email, password):
        self._email = email
        self._password = password



game1 = Game("The Witcher 3: Wild Hunt", 29.99)
game2 = Game("Red Dead Redemption 2", 49.99)
game3 = Game("Football Manager 2023", 1459)
game4 = Game("Hogwarts Legacy", 1590)
game5 = Game("The Legend of Zelda", 1790)

user1 = User("JohnDoe", "password123", "johndoe@example.com", 1)


user1.add_credit_card(card_name='credit1',card_number="1234567812345678", expiration="12/24", cvv="123")
user1.add_credit_card(card_name='credit2',card_number="9876543212345678", expiration="12/22", cvv="352")
user1.add_paypal(email="sunpolll@gmail.com", password="ps")


cart1 = Cart(user_id = 1)
cart1.add_game(game1)
cart1.add_game(game2)

purchase1 = Purchase(user_id = 1)

class GameName(BaseModel):
    name: str

@app.post("/users/{user_id}/your_payment")
async def pay_with_your_own_method(user_id:int,payment_type:str,card_name:str):
    purchase = Purchase.user_purchase[user_id]
    return purchase.own_card(payment_type,card_name)
@app.post("/users/{user_id}/creditcard")
async def pay_with_credit_card(user_id:int,card_name:str,card_number:int, expiration:str, cvv:int, save_status:str):
    purchase = Purchase.user_purchase[user_id]
    return purchase.pay_with_credit_card(card_name,card_number, expiration, cvv, save_status)
@app.post("/users/{user_id}/paypal")
async def pay_with_paypal(user_id:int,email:str, password:int, save_status:str):
    purchase = Purchase.user_purchase[user_id]
    return purchase.pay_wtih_paypal(email, password, save_status)
@app.get("/users/{user_id}/payment_method")
async def watch_payment_method(user_id:int):
    user = User.users[user_id]
    pm = []
    for x in user._credit_card:
        cd = user._credit_card[x]
        pm.append(f"Card_name:{x}  Card_number:{cd._card_number}")
    for x in user._paypal:
        pm.append(f"Paypal_email:{x}")
    return "   |   ".join(pm)

@app.get("/users/{user_id}/purcahse_history")
async def watch_purchase_history(user_id:int):
    user = User.users[user_id]
    allgm = []
    for gm in user._purchase_history:
        game = user._purchase_history[gm]
        allgm.append(f"Game_name:{gm}  Game_price:{game}")
    return "   |   ".join(allgm)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1",port=8000)

