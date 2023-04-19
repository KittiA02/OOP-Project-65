from fastapi import FastAPI
from pydantic import BaseModel
from main import *
import uvicorn

app = FastAPI()

user1 = User("john_doe", "password123", "john_doe@example.com", 1)
# FastAPI route handlers
@app.get("/games")
async def get_games():
    game_dicts = [game.to_dict() for game in games]
    return game_dicts

# FastAPI route handlers for wishlist
@app.post("/users/{user_id}/wishlist/add_game")
async def add_game_to_wishlist(user_id: int, game_index: int):
    wishlist = Wishlist.wishlists[user_id]
    game = games[game_index]
    return wishlist.add_game(game)

@app.post("/users/{user_id}/wishlist/remove_game")
async def remove_game_from_wishlist(user_id: int, game_index: int):
    wishlist = Wishlist.wishlists[user_id]
    game = games[game_index]
    return wishlist.remove_game(game)

@app.get("/users/{user_id}/wishlist/view_wishlist")
async def view_wishlist(user_id: int):
    wishlist = Wishlist.wishlists[user_id]
    return wishlist.view_wishlist()

@app.post("/users/{user_id}/cart/add_game")
async def add_game_to_cart(user_id: int, game_index: int):
    cart = Cart.carts[user_id]
    game = games[game_index]
    return cart.add_game(game)

@app.post("/users/{user_id}/cart/remove_game")
async def remove_game_from_cart(user_id: int, game_index: int):
    cart = Cart.carts[user_id]
    game = games[game_index]
    return cart.remove_game(game)

@app.get("/users/{user_id}/cart/view_cart")
async def view_cart(user_id: int):
    cart = Cart.carts[user_id]
    return cart.view_cart()

@app.get("/users/{user_id}/cart/total_price")
async def get_total_price(user_id: int):
    cart = Cart.carts[user_id]
    return {"total_price": cart.total_price()}

# FastAPI route handlers for payment
@app.post("/users/{user_id}/payment/pay_with_credit_card")
async def make_payment_with_credit_card(user_id: int, card_name: str, card_number: str, expiration: str, cvv: str, save_status: str):
    purchase = Purchase.user_purchase[user_id]
    return purchase.pay_with_credit_card(card_name,card_number, expiration, cvv, save_status)

@app.post("/users/{user_id}/payment/pay_with_paypal")
async def make_payment_with_paypal(user_id: int, email: str, password: str, save_status: str):
    purchase = Purchase.user_purchase[user_id]
    return purchase.pay_with_paypal(email, password, save_status)

@app.post("/users/{user_id}/payment/use_own_card")
async def make_payment_with_own_card(user_id: int, payment_type: str, card_name: str):
    purchase = Purchase.user_purchase[user_id]
    return purchase.own_card(payment_type, card_name)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)