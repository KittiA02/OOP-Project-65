import json
from fastapi import FastAPI
import uvicorn

app = FastAPI()

class Game:
    def __init__(self, name, price, detail):
        self.name = name
        self.price = price
        self.detail = detail

class GameList:
    def __init__(self):
        self.list = []

    def add_to_list(self, game):
        self.list.append(game)

    def __str__(self):
        return '\n'.join(game.name for game in self.list)
    
    def __getitem__(self, index):
        return self.list[index]

class Cart:
    def __init__(self):
        self.cart = []

    def add_game(self, game):
        self.cart.append(game)
        return {"message": f"Added {game.name} to cart."}

    def remove_game(self, game):
        if game in self.cart:
            self.cart.remove(game)
            return {"message": f"Removed {game.name} from cart."}
        else:
            return {"error": "GameNotFound"}

    def view_cart(self):
        if len(self.cart) == 0:
            return {"message": "Your cart is empty."}
        else:
            games = [{"name": game.name, "price": game.price} for game in self.cart]
            return {"games": games}

    def total_price(self):
        return sum(game.price for game in self.cart)

list1 = GameList()
cart1 = Cart()

@app.get("/games")
async def get_games():
    return {"games": [{"name": game.name, "price": game.price, "detail": game.detail} for game in list1.list]}

@app.post("/cart/add_game")
async def add_game_to_cart(game_index: int):
    game = list1[game_index]
    return cart1.add_game(game)

@app.post("/cart/remove_game")
async def remove_game_from_cart(game_index: int):
    game = list1[game_index]
    return cart1.remove_game(game)

@app.get("/cart/view_cart")
async def view_cart():
    return cart1.view_cart()

@app.get("/cart/total_price")
async def get_total_price():
    return {"total_price": cart1.total_price()}

# Function to handle adding a game to the cart
@app.post("/cart/add_to_cart")
async def add_to_cart(game_index: int):
    game = list1[game_index]
    cart1.add_game(game)
    return {"message": f"Added {game.name} to cart."}

# Function to handle displaying the contents of the cart
@app.get("/cart/view_cart")
async def view_cart():
    return cart1.view_cart()

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)
