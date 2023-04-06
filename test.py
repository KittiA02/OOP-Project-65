from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class User:
    users = {}
    def __init__(self, username, password, email, user_id):
        self._username = username
        self._password = password
        self._email = email
        self._user_id = user_id
        self._payment_method = []
        self._purchase_history = []
        self._wish_list = []
        User.users[self._user_id] = self

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_email(self, email):
        self._email = email 

    def add_to_wishlist(self, game_name):
        game = Game.games[game_name]
        self._wish_list.append(game)

    def remove_from_wishlist(self, game_name):
        for game in self._wish_list:
            if game._name == game_name:
                self._wish_list.remove(game)
                return 1
        return 0

    def add_to_cart(self, cart, game_name):
        if game_name in Game.games :
            game = Game.games[game_name]
            if game not in self._wish_list :
                return -1
            elif game in cart._games :
                return -2
            else :
                cart.add_item(game)
        else :
            return 0

class Game:
    games = {}
    def __init__(self, name, price):
        self._name = name
        self._price = price

        Game.games[self._name] = self

class Cart:
    def __init__(self):
        self._games = []

    def add_item(self, game):
        self._games.append(game)

    def remove_item(self, game):
        self._games.remove(game)

    def calculate_total(self):
        total = 0
        for game in self._games:
            total += game._price
        return total


game1 = Game("Football Manager 2023", 1459)
game2 = Game("Hogwarts Legacy", 1590)
game3 = Game("The Legend of Zelda", 1790)

user1 = User("john_doe", "password123", "john_doe@example.com", 1)

cart = Cart()

class GameName(BaseModel):
    name: str

@app.post("/users/{user_id}/wishlist")
async def add_game_to_wishlist(user_id: int, game_name: str):
    user = User.users[user_id]
    if game_name in Game.games :
        user.add_to_wishlist(game_name)
        return {"message": "Game added to wishlist."}
    else :
        return {"message": "Game not found."}

@app.delete("/users/{user_id}/wishlist")
async def remove_game_from_wishlist(user_id: int, game_name: str):
    user = User.users[user_id]
    if user.remove_from_wishlist(game_name) == 1 :
        return {"message": "Game removed from wishlist."}
    else :
        return {"message": "Game not found."}

@app.post("/users/{user_id}/cart")
async def add_game_to_cart(user_id: int, game_name: str):
    user = User.users[user_id]
    num = user.add_to_cart(cart, game_name)
    if num == 0 :
        return {"message": "Game not found."}
    elif num == -1 :
        return {"message": "Game not found in your Wishlist"}
    elif num == -2 :
        return {"message": "Game already in your cart"}
    else :
        return {"message": "Game added to your cart"}

@app.get("/users/{user_id}/wishlist")
async def display_wishlist(user_id: int):
    user = User.users[user_id]
    wishlist = [game._name for game in user._wish_list]
    return {"wishlist": wishlist}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)