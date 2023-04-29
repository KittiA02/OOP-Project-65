from fastapi import FastAPI
from typing import List
import uvicorn

app = FastAPI()

class Game:
    def __init__(self, name: str, price: float, details: str, image_url: str):
        self.name = name
        self.price = price
        self.details = details
        self.image_url = image_url

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "price": self.price,
            "details": self.details,
            "image_url": self.image_url
        }

class Games:
    def __init__(self, games: List[Game]):
        self.games = games

    def get_game_info(self) -> List[dict]:
        game_dicts = [game.to_dict() for game in self.games]
        return game_dicts

game_lists = [
        Game("Grand Theft Auto V", 1850, "Open-world action-adventure game.", "https://cdn.cloudflare.steamstatic.com/steam/apps/271590/capsule_616x353.jpg"),
        Game("Minecraft", 790, "Sandbox game where you can build and explore.", "https://image.api.playstation.com/vulcan/img/cfn/11307uYG0CXzRuA9aryByTHYrQLFz-HVQ3VVl7aAysxK15HMpqjkAIcC_R5vdfZt52hAXQNHoYhSuoSq_46_MT_tDBcLu49I.png"),
        Game("Fortnite", 0, "A FREE Battle royale game with cartoon graphics.", "https://cdn1.epicgames.com/offer/fn/24BR_S24_EGS_Launcher_Blade_2560x1440_2560x1440-437d0424d02f5fd286ab659ddade30db"),
        Game("Hogwarts Legacy", 1500, "Single-player Action-adventure game", "https://cdn1.epicgames.com/offer/e97659b501af4e3981d5430dad170911/EGS_HogwartsLegacy_AvalancheSoftware_S1_2560x1440-2baf3188eb3c1aa248bcc1af6a927b7e"),
        Game("The Elder Scrolls V: Skyrim", 1400, "Single-player Action game", "https://cdn1.epicgames.com/offer/c8738a4d1ead40368eab9688b3c7d737/EGS_TheElderScrollsVSkyrimAnniversaryEdition_BethesdaGameStudios_Editions_S1_2560x1440-accc22362e1ae7bf4c1fe215f357c5a6"),
        Game("Fall Guys", 500, "A battle royale game", "https://cdn1.epicgames.com/offer/50118b7f954e450f8823df1614b24e80/EGS_FallGuys_Mediatonic_S1_2560x1440-187aa50ffaa014885d6702a0b632f848"),
        Game("Among Us", 120, "A multiplayer game where you work together to find the imposter on a spaceship", "https://cdn1.epicgames.com/salesEvent/salesEvent/amoguslandscape_2560x1440-3fac17e8bb45d81ec9b2c24655758075"),
        Game("Phasmophobia", 350, "A horror game where you and your team investigate haunted locations and try to capture evidence of ghosts", "https://cdn.cloudflare.steamstatic.com/steam/apps/739630/capsule_616x353.jpg?t=1674232976"),
        Game("The Legend of Zelda: Breath of the Wild", 2000, "Action-adventure game in an open world environment.", "https://assets.nintendo.com/image/upload/v1681238674/Microsites/zelda-tears-of-the-kingdom/videos/posters/totk_microsite_officialtrailer3_1304xj47am"),
        Game("Overwatch", 990, "Multiplayer first-person shooter game", "https://upload.wikimedia.org/wikipedia/en/thumb/5/51/Overwatch_cover_art.jpg/220px-Overwatch_cover_art.jpg"),
        Game("Portal 2", 100, "First-person puzzle-platform game.", "https://cdn.akamai.steamstatic.com/steam/apps/620/header.jpg"),
        Game("Red Dead Redemption 2", 2200, "Action-adventure game in an open world environment.", "https://cdn1.epicgames.com/b30b6d1b4dfd4dcc93b5490be5e094e5/offer/RDR2476298253_Epic_Games_Wishlist_RDR2_2560x1440_V01-2560x1440-2a9ebe1f7ee202102555be202d5632ec.jpg"),
        Game("The Witcher 3: Wild Hunt", 1290, "Action role-playing game with an open world environment", "https://cdn1.epicgames.com/offer/14ee004dadc142faaaece5a6270fb628/EGS_TheWitcher3WildHuntCompleteEdition_CDPROJEKTRED_S1_2560x1440-82eb5cf8f725e329d3194920c0c0b64f"),
        Game("Assassin's Creed Valhalla", 1700, "Action role-playing game with an open world environment", "https://cdn1.epicgames.com/salesEvent/salesEvent/UK_ACV_DELUXE%20_EPIC_Store%20Landscape_2560x1440%20_2560x1440-0585cdaf65bee5ffce91881220ade66b"),
        Game("Call of Duty: Warzone", 0, "A FREE first-person shooter battle royale game with 150 players.", "https://www.callofduty.com/content/dam/atvi/callofduty/cod-touchui/blog/hero/mw-wz/WZ-Season-Three-Announce-TOUT.jpg"),
        Game("Counter-Strike: Global Offensive", 0, "A FREE multiplayer first-person shooter game.", "https://cdn.cloudflare.steamstatic.com/steam/apps/730/capsule_616x353.jpg?t=1668125812"),
        Game("Starcraft II", 1190, "A sci-fi real-time strategy game.", "https://s.isanook.com/ga/0/rp/r/w850/ya0xa0m1w0/aHR0cHM6Ly9zLmlzYW5vb2suY29tL2dhLzAvdWQvMjE1LzEwNzc5NDcvc3RhcmNyYWZ0aWkoMSkuanBn.jpg"),    
        Game("Fallout 4", 450, "Open-world post-apocalyptic action role-playing game.", "https://image.api.playstation.com/vulcan/ap/rnd/202009/2500/4GZyUQ1bHTjICP6GCRG7f65n.png"),
        Game("World of Warcraft", 1590, "An online multiplayer RPG set in the Warcraft universe.", "https://cdn.wccftech.com/wp-content/uploads/2016/10/world-of-warcraft-vanilla-legacy.jpg"),    
        Game("Civilization VI", 790, "A turn-based strategy game where you build an empire to stand the test of time.", "https://cdn2.unrealengine.com/2kgcap-civ-6-new-frontier-screenshots-silver-corporation-02-3840x2160-73ea9642c337.png"),    
        Game("Cities: Skylines", 390, "A modern take on the classic city simulation.", "https://cdn1.epicgames.com/6009be9994c2409099588cde6f3a5ed0/offer/EGS_CitiesSkylines_ColossalOrder_S3-2560x1440-14df106873c918591e49bd9604841e83.jpg"),    
        Game("Stardew Valley", 250, "A farming simulation game with RPG elements.", "https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/en_US/games/switch/s/stardew-valley-switch/hero"),    
        Game("Subnautica", 450, "An underwater adventure game where you explore a vast alien ocean.", "https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/en_US/games/switch/s/subnautica-switch/hero"),
]

games = Games(game_lists)

# FastAPI route handlers
@app.get("/games")
async def show_game_info():
    return games.get_game_info()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)