from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from backendclass import *
app = FastAPI()



# Game list
games = [
    Game("Grand Theft Auto V", 1850, "Open-world action-adventure game.", "https://cdn.cloudflare.steamstatic.com/steam/apps/271590/capsule_616x353.jpg"),
        Game("Minecraft", 790, "Sandbox game where you can build and explore as you like.", "https://image.api.playstation.com/vulcan/img/cfn/11307uYG0CXzRuA9aryByTHYrQLFz-HVQ3VVl7aAysxK15HMpqjkAIcC_R5vdfZt52hAXQNHoYhSuoSq_46_MT_tDBcLu49I.png"),
        Game("Fortnite", 0, "A Battle royale game with cartoon graphics.", "https://cdn1.epicgames.com/offer/fn/24BR_S24_EGS_Launcher_Blade_2560x1440_2560x1440-437d0424d02f5fd286ab659ddade30db"),
        Game("Hogwarts Legacy", 1500, "Single-player Action-adventure game", "https://cdn1.epicgames.com/offer/e97659b501af4e3981d5430dad170911/EGS_HogwartsLegacy_AvalancheSoftware_S1_2560x1440-2baf3188eb3c1aa248bcc1af6a927b7e"),
        Game("The Elder Scrolls V: Skyrim", 1400, "Single-player Action game", "https://cdn1.epicgames.com/offer/c8738a4d1ead40368eab9688b3c7d737/EGS_TheElderScrollsVSkyrimAnniversaryEdition_BethesdaGameStudios_Editions_S1_2560x1440-accc22362e1ae7bf4c1fe215f357c5a6"),
        Game("Fall Guys", 500, "A cartoon-like character battle royale game", "https://cdn1.epicgames.com/offer/50118b7f954e450f8823df1614b24e80/EGS_FallGuys_Mediatonic_S1_2560x1440-187aa50ffaa014885d6702a0b632f848"),
        Game("Among Us", 120, "A multiplayer game where you work together to find the imposter on a spaceship", "https://cdn1.epicgames.com/salesEvent/salesEvent/amoguslandscape_2560x1440-3fac17e8bb45d81ec9b2c24655758075"),
        Game("Phasmophobia", 350, "A horror game where you and your team\n investigate haunted locations\n and try to capture evidence of ghosts", "https://cdn.cloudflare.steamstatic.com/steam/apps/739630/capsule_616x353.jpg?t=1674232976"),
        Game("The Legend of Zelda: Breath of the Wild", 2000, "Action-adventure game in an open world environment from Nintendo platform.", "https://assets.nintendo.com/image/upload/v1681238674/Microsites/zelda-tears-of-the-kingdom/videos/posters/totk_microsite_officialtrailer3_1304xj47am"),
        Game("Overwatch", 990, "Multiplayer role-playing first-person shooter game", "https://upload.wikimedia.org/wikipedia/en/thumb/5/51/Overwatch_cover_art.jpg/220px-Overwatch_cover_art.jpg"),
        Game("Portal 2", 100, "First-person puzzle-platform game that can done in multi-player mode.", "https://cdn.akamai.steamstatic.com/steam/apps/620/header.jpg"),
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
        Game("League of Legends", 0, "Multiplayer online battle arena game.", "https://cdn1.epicgames.com/offer/24b9b5e323bc40eea252a10cdd3b2f10/LOL_2560x1440-98749e0d718e82d27a084941939bc9d3"),
        Game("Valorant", 0, "Free-to-play first-person shooter game.", "https://www.riotgames.com/darkroom/1440/d0807e131a84f2e42c7a303bda672789:3d02afa7e0bfb75f645d97467765b24c/valorant-offwhitelaunch-keyart.jpg"),
        Game("Apex Legends", 0, "Free-to-play battle royale first-person shooter game.", "https://media.contentapi.ea.com/content/dam/apex-legends/images/2019/01/apex-featured-image-16x9.jpg.adapt.crop16x9.1023w.jpg"),
        Game("FIFA 22", 599, "Soccer simulation game.", "https://cdn.cloudflare.steamstatic.com/steam/apps/1506830/capsule_616x353.jpg?t=1678115961"),
        Game("NBA 2K22", 599, "Basketball simulation game.", "https://cdn.cloudflare.steamstatic.com/steam/apps/1644960/header.jpg?t=1660885243"),
        Game("Rocket League", 0, "Vehicular soccer video game.", "https://cdn1.epicgames.com/offer/9773aa1aa54f4f7b80e44bef04986cea/EGS_RocketLeague_PsyonixLLC_S3_2560x1440-1434001758900f513cab0c885121744a"),
        Game("Rainbow Six Siege", 1999, "First-person shooter game with multiplayer modes.", "https://cdn.cloudflare.steamstatic.com/steam/apps/359550/capsule_616x353.jpg?t=1680010421"),
        Game("Dead by Daylight", 499, "Survival horror game with multiplayer modes.\n (Killer and Survivor, each role have each objective to do and win the game)", "https://cdn1.epicgames.com/offer/611482b8586142cda48a0786eb8a127c/EGS_DeadbyDaylight_BehaviourInteractive_S1_2560x1440-a32581cf9948a9a2e24b2ff15c1577c7"),
        Game("The Sims 4", 0, "Life simulation game that let player control them.", "https://www.appdisqus.com/wp-content/uploads/2022/09/sims-4-update-patch-notes-e0b8a7e0b8b1e0b899e0b899e0b8b5e0b989-25-e0b8a1e0b881e0b8a3e0b8b2e0b884e0b8a1-1600x900.jpg.webp"),
        Game("Genshin Impact", 0, "Free-to-play action role-playing game\nwith free open-world environment and unique story to explore.", "https://cdn1.epicgames.com/salesEvent/salesEvent/EGS_GenshinImpact_miHoYoLimited_S1_2560x1440-91c6cd7312cc2647c3ebccca10f30399"),
        Game("Monster Hunter Rise", 599, "Action role-playing game where players hunt monsters.", "https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000029016/b6ca09e9a7f6faf27641f62dabe64c6ff97b4f326aa478379e3c112aa28eb9ab"),
        Game("Among Trees", 199, "Open-world survival game in a forest setting.", "https://cdn1.epicgames.com/offer/1886704a76f94324ab964a4698db3e09/EGS_AmongTrees_FJRDInteractive_NEW_2560x1440-900992410fbb6ad8528e2cc03140b6f5"),
]
catalog = Catalog()

for game in games:
    catalog.add_game(game)

usermanage = UserManager()
authentication = Authentication(usermanage)

system_users = [
    authentication.sign_up('Jem',123,'nongjem@gmail.com'),
    authentication.sign_up('Shan',123,'nongshan@gmail.com'),
    authentication.sign_up('Beam',123,'nongbeam@gmail.com'),
    authentication.sign_up('Pooh',123,'nongpooh@gmail.com')
]

user = usermanage.search_user(2)
cc1 = CreditCard('Pollawat Prechathaamruch',123456789,'11.24',352)
pp1 = Paypal('64011201@kmitl.ac.th',12345)
user.payment_info.add_credit_card(cc1)
user.payment_info.add_paypal(pp1)
pay = Purchase(user)
pay.one_purchase_CC(catalog.search_games('Minecraft'),cc1,False)

#Authentication
@app.post("/sign_up", tags=["Authentication"])
async def sign_up(data : dict):
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    signup = authentication.sign_up(username, password, email)
    if signup != False: return signup.user_info.user_id
    else : return False

@app.post("/login", tags=["Authentication"])
async def login(data: dict):
    username = data.get("username")
    password = data.get("password")
    logged_in = authentication.login(username, password)
    if logged_in != False:
        return logged_in.user_info.user_id
    else:
        return False


#Game
@app.get("/", tags=["Homepage"])
async def get_all_games():
    games_list = catalog.games
    return games_list

#Users
@app.get("/user/user_info/{user_id}", tags=["User Info"])
async def get_user(user_id : int):
    user = usermanage.search_user(user_id)
    return user.user_info

@app.get("/user/payment_info/{user_id}", tags=["Payment Info"])
async def get_user(user_id : int):
    user = usermanage.search_user(user_id)
    return user.payment_info
@app.get("/user/shopping_info/{user_id}", tags=["Shopping Info"])
async def get_user(user_id : int):
    user = usermanage.search_user(user_id)
    return user.shopping_info.purchase_history.purchased
@app.post("/user/add_credit_card/{user_id}", tags=["User Info"])
async def get_user(data : dict):
    user = usermanage.search_user(data["user_id"])
    name = data['name']
    card_number = data['card_number']
    exp = data['exp']
    cvv = data['cvv']
    user.payment_info.add_credit_card(CreditCard(name, card_number, exp, cvv))
    return user.payment_info

@app.delete("/user/remove_credit_card/{user_id}", tags=["User Info"])
async def get_user(data : dict):
    user = usermanage.search_user(data["user_id"])
    card_name = data['card_name']
    user.payment_info.remove_credit_card(card_name)
    return user.payment_info

@app.post("/user/add_paypal/{user_id}", tags=["User Info"])
async def get_user(data : dict):
    user = usermanage.search_user(data["user_id"])
    email = data['email']
    password = data['password']
    user.payment_info.add_paypal(Paypal(email, password))
    return user.payment_info
    
@app.delete("/user/remove_paypal/{user_id}", tags=["User Info"])
async def get_user(data : dict):
    user = usermanage.search_user(data["user_id"])
    email = data['email']
    user.payment_info.remove_paypal(email)
    return user.payment_info

@app.post("/user/update_user_info/{user_id}", tags=["User Info"])
async def get_user(data : dict):
    user = usermanage.search_user(data["user_id"])
    if data["username"] != '':
        user.user_info.username = data["username"]
    if data["password"] != '':
        user.user_info.password = data["password"]
    if data["email"] != '':
        user.user_info.email = data["email"]
    return user.user_info
#Shoppingcart
@app.get("/cart/{user_id}", tags=["Shoppingcart"])
async def view_cart(user_id : int):
    user = usermanage.search_user(user_id)
    return user.shopping_info.user_cart.items 

@app.get("/cart/get_total_price/{user_id}", tags=["Shoppingcart"])
async def get_total_price(user_id : int):
    user = usermanage.search_user(user_id)
    return user.shopping_info.user_cart.get_total_price()

@app.post("/cart/add_to_cart/{user_id}/{game_title}", tags=["Shoppingcart"])
async def add_to_cart(user_id : int, game_title : str):
    user = usermanage.search_user(user_id)
    user.shopping_info.user_cart.add_item(catalog.search_games(game_title))
    return f"{game_title} added to cart"

@app.delete("/cart/remove_from_cart/{user_id}/{game_title}", tags=["Shoppingcart"])
async def remove_from_cart(user_id : int, game_title : str):
    user = usermanage.search_user(user_id)
    user.shopping_info.user_cart.remove_item(catalog.search_games(game_title))
    return f"{game_title} deleted to cart"
#Wishlist
@app.get("/wishlist/{user_id}", tags=["Wishlist"])
async def view_wishlist(user_id:int):
    user = usermanage.search_user(user_id)
    return user.shopping_info.user_wishlist.items

@app.post("/wishlist/add_to_wishlist/{user_id}/{game_title}", tags=["Wishlist"])
async def add_to_wishlist(user_id : int, game_title : str):
    user = usermanage.search_user(user_id)
    user.shopping_info.user_wishlist.add_item(catalog.search_games(game_title))
    return f"{game_title} added to wishlist"

@app.delete("/wishlist/remove_from_wishlist/{user_id}/{game_title}", tags=["Wishlist"])
async def remove_from_wishlist(user_id : int, game_title : str):
    user = usermanage.search_user(user_id)
    user.shopping_info.user_wishlist.remove_item(catalog.search_games(game_title))
    return f"{game_title} removed from wishlist"

@app.post("/payment/creditcard/{user_id}",tags= ["Pay with credit card"])
async def pay_cc(data : dict):
    user_id = data['user_id']
    name = data['name']
    card_number = data['card_number']
    expiration = data['expiration']
    cvv = data['cvv']
    save = data['save']
    game_title = data['game_title']
    current_user = usermanage.search_user(user_id)
    current_card = CreditCard(name,card_number,expiration,cvv)
    current_purchase = Purchase(current_user)
    if game_title == 'no':
        current_purchase.cart_purchase_CC(current_card,save)
        current_user.shopping_info.user_cart.items = {}
    else:
        game = catalog.search_games(game_title)
        current_purchase.one_purchase_CC(game,current_card,save)
    return f'Your Purchase is successfully'
    

@app.post("/payment/paypal/{user_id}",tags= ["Pay with Paypal"])
async def pay_cc(data : dict):
    user_id = data['user_id']
    email = data['email']
    password = data['password']
    save = data['save']
    game_title = data['game_title']

    current_user = usermanage.search_user(user_id)
    current_pp = Paypal(email,password)
    current_purchase = Purchase(current_user)
    if game_title == 'no':
        current_purchase.cart_purchase_PP(current_pp,save)
        current_user.shopping_info.user_cart.items = {}
    else:
        game = catalog.search_games(game_title)
        current_purchase.one_purchase_PP(game,current_pp,save)
    return f'Your Purchase is successfully'

# python3 -m uvicorn api:app --reload
