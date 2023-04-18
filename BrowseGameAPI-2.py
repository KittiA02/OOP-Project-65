from fastapi import FastAPI

app = FastAPI()

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

@app.get("/games")
async def get_games():
    game_dicts = [game.to_dict() for game in games]
    return game_dicts
