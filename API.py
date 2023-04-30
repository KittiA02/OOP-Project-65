from fastapi import FastAPI
from pydantic import BaseModel
from test_demo import *
import uvicorn

app = FastAPI()

class GameSearch(BaseModel):
    query: str

@app.get("/", tags=["Homepage"])
async def get_all_games():
    games_dict = []
    for game in catalog.games:
        games_dict.append(game.title)
    return games_dict

@app.get("/game/{game_title}", tags=["Games"])
async def get_game(game_title: str):
    game = catalog.search_games(game_title)
    if game:
        return game
    else:
        return {"error": "Game not found"}

@app.get("/users", tags=["Users"])
async def get_users():
    return [{"user_id": user.user_info.user_id, "username": user.user_info.username} for user in UserManager().users]

@app.get("/user/{user_id}", tags=["Users"])
async def get_user(user_id: int):
    for user in UserManager().users:
        if user.user_info.user_id == user_id:
            return {"user_id": user.user_info.user_id, "username": user.user_info.username}
    return {"error": "User not found"}

@app.post("/search_game", tags=["Games"])
async def search_game(title: dict):
    game = catalog.search_games(title["game"])
    if game:
        return {game.title}
    else:
        return {"error": "Game not found"}
