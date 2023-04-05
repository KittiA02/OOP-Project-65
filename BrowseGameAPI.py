from fastapi import FastAPI, APIRouter
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import uvicorn

router = APIRouter()

class Game:
    def __init__(self, name, price, details):
        self.name = name
        self.price = price
        self.details = details
        
    def get_info(self):
        return f"{self.name} ({self.price} Baht) - {self.details}"

class GameList:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def browse_games(self):
        return [game.get_info() for game in self.games]

class GameCatalog:
    def __init__(self, game_list):
        self.game_list = game_list
        
    def display_games(self):
        game_info = [f"{game.name} ({game.price} Baht) - {game.details}" for game in self.game_list.games]
        return "\n".join(game_info)

    def get_game_by_name(self, name):
        for game in self.game_list.games:
            if game.name == name:
                return {"name": game.name, "price": game.price, "details": game.details}
        return None
    
    def add_game(self, game):
        self.game_list.add_game(game)

# Example usage:
game1 = Game("GTA V", 1850, "Open-world action-adventure game.")
game2 = Game("Minecraft", 790, "Sandbox game where you can build and explore.")
game3 = Game("Fortnite", 0, "Battle royale game with cartoon graphics.")
game4 = Game('Hogwart', 1500, 'Single-player Action-adventure game')
game5 = Game('Skyrim', 1400, 'Single-player Action game')
game6 = Game('Destiny', 900, 'Multi-player FPS game')

game_list = GameList()
game_list.add_game(game1)
game_list.add_game(game2)
game_list.add_game(game3)
game_list.add_game(game4)
game_list.add_game(game5)
game_list.add_game(game6)

# Create a game catalog using the game list
catalog = GameCatalog(game_list)

# Create a FastAPI app
app = FastAPI()
app.include_router(router)

# Define an endpoint to display all the games in the catalog
@app.get("/games")
def display_games():
    return catalog.display_games()

# Define an endpoint to get a game by name
@app.get("/games/{name}")
def get_game_by_name(name: str):
    game = catalog.get_game_by_name(name)
    if game is not None:
        return game
    else:
        return {"error": "Game not found."}

# Define an endpoint to add a game to the catalog
class GameInput(BaseModel):
    name: str
    price: int
    details: str

@app.post("/games")
def add_game(game: GameInput):
    new_game = Game(game.name, game.price, game.details)
    catalog.add_game(new_game)
    return JSONResponse(content=catalog.display_games(), indent=4)

@app.get("/games/{name}")
def get_game_by_name(name: str):
    game = catalog.get_game_by_name(name)
    if game is not None:
        return game
    else:
        return {"error": "Game not found."}


# Run the FastAPI app using the uvicorn server
if __name__ == "__main__":
    uvicorn.run(app, host="172.20.10.4", port=8000)
