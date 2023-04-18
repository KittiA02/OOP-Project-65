from fastapi import FastAPI

app = FastAPI()

games = [
    {
        "name": "GTA V",
        "price": 1850,
        "description": "Open-world action-adventure game.",
    },
    {
        "name": "Minecraft",
        "price": 790,
        "description": "Sandbox game where you can build and explore.",
    },
    {
        "name": "Fortnite",
        "price": 0,
        "description": "A FREE Battle royale game with cartoon graphics.",
    },
    {
        "name": "Hogwart",
        "price": 1500,
        "description": "Single-player Action-adventure game",
    },
    {
        "name": "Skyrim",
        "price": 1400,
        "description": "Single-player Action game",
    },
    {
        "name": "Destiny",
        "price": 900,
        "description": "Multi-player FPS game",
    },
    {
        "name": "Fall Guys",
        "price": 500,
        "description": "A battle royale game",
    },
    {
        "name": "Among Us",
        "price": 120,
        "description": "A multiplayer game where you work together to find the imposter on a spaceship",
    },
    {
        "name": "Valheim",
        "price": 280,
        "description": "A Viking-themed survival game where you explore and build in a procedurally generated world",
    },
    {
        "name": "Phasmophobia",
        "price": 350,
        "description": "A horror game where you and your team investigate haunted locations and try to capture evidence of ghosts",
    },
]

@app.get("/games")
async def get_games():
    return games
