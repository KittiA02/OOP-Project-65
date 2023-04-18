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
        print("Game Catalog:")
        for game in self.game_list.games:
            print(f"{game.name} ({game.price} Baht)")

    def get_game_by_name(self, name):
        for game in self.game_list.games:
            if game.name == name:
                return game
        return None

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

# Display all the games in the catalog
catalog.display_games()

# Prompt the user to enter the name of the game they want to view
game_name = input("\nName of the game you want to view: ")

game = catalog.get_game_by_name(game_name)

if game is not None:
    print("\nGame found:")
    print(game.get_info())
    print("\n")
else:
    print("\nGame not found.")
    print("\n")