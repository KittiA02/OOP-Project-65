import tkinter as tk
class Game:
    def __init__(self, name, price, details):
        self.name = name
        self.price = price
        self.details = details

    def get_info(self):
        return f"{self.name} ({self.price} Baht) - {self.details}"

class GameButton(tk.Button):
    def __init__(self, master, game, row, column, command=None):
        super().__init__(
            master, text=game.name, font=("Open Sans", 16, "bold"), width=15, height=3, command=command,
            wraplength=200
        )
        self.game = game
        self.grid(row=row, column=column, padx=10, pady=10)

class GameCatalogApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Epic Game Store")

        self.label = tk.Label(
            self.master, text="Featured Game Today", font=("Open Sans", 36, "bold")
        )
        self.label.grid(row=0, column=0, pady=(25,0))
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.grid(row=1, column=0, pady=20, sticky="nsew")

        self.buttons = []

        # Example game data
        games = [
            Game("Grand Theft Auto V", 1850, "Open-world action-adventure game."),
            Game("Minecraft", 790, "Sandbox game where you can build and explore."),
            Game("Fortnite", 0, "A FREE Battle royale game with cartoon graphics."),
            Game("Hogwarts Legacy", 1500, "Single-player Action-adventure game"),
            Game("The Elder Scrolls V: Skyrim", 1400, "Single-player Action game"),
            Game("Fall Guys", 500, "A battle royale game"),
            Game("Among Us", 120, "A multiplayer game where you work together to find the imposter on a spaceship"),
            Game("Valheim", 280, "A Viking-themed survival game where you explore and build in a procedurally generated world"),
            Game("Phasmophobia", 350, "A horror game where you and your team investigate haunted locations and try to capture evidence of ghosts"),
            Game("The Legend of Zelda: Breath of the Wild", 2000, "Action-adventure game in an open world environment."),
            Game("Overwatch", 990, "Multiplayer first-person shooter game"),
            Game("Portal 2", 100, "First-person puzzle-platform game."),
            Game("Red Dead Redemption 2", 2200, "Action-adventure game in an open world environment."),
            Game("The Witcher 3: Wild Hunt", 1290, "Action role-playing game with an open world environment"),
            Game("Assassin's Creed Valhalla", 1700, "Action role-playing game with an open world environment"),
            Game("Call of Duty: Warzone", 0, "A FREE first-person shooter battle royale game with 150 players."),
            Game("Counter-Strike: Global Offensive", 0, "A FREE multiplayer first-person shooter game."),
            Game("Overwatch", 990, "A team-based multiplayer first-person shooter."),    
            Game("Starcraft II", 1190, "A sci-fi real-time strategy game."),    
            Game("Fallout 4", 450, "Open-world post-apocalyptic action role-playing game."),
            Game("World of Warcraft", 1590, "An online multiplayer RPG set in the Warcraft universe."),    
            Game("Civilization VI", 790, "A turn-based strategy game where you build an empire to stand the test of time."),    
            Game("Cities: Skylines", 390, "A modern take on the classic city simulation."),    
            Game("Stardew Valley", 250, "A farming simulation game with RPG elements."),    
            Game("Subnautica", 450, "An underwater adventure game where you explore a vast alien ocean."),

        ]

        for i, game in enumerate(games):
            column = i % 5
            row = i // 5
            game = Game(game.name, game.price, game.details)
            button = GameButton(
                self.buttons_frame, game, row, column, lambda game=game: self.show_game_info(game)
            )
            self.buttons.append(button)

    def show_game_info(self, game):
        details_window = tk.Toplevel(self.master)
        details_window.title(game.name)
        details_window.geometry("400x300")
        
        game_name = tk.Label(
            details_window, text=game.name.upper(), font=("Open Sans", 24, "bold"), wraplength=400
        )
        game_name.pack(pady=(20, 10))
        
        game_price_frame = tk.Frame(details_window)
        game_price_frame.pack()

        price_label = tk.Label(game_price_frame, text="Price: ", font=("Open Sans", 18, "bold"))
        price_label.pack(side=tk.LEFT)

        price_value_label = tk.Label(game_price_frame, text=f"{game.price} Baht", font=("Open Sans", 16))
        price_value_label.pack(side=tk.LEFT)

        game_details = tk.Label(
            details_window, text=game.details, font=("Open Sans", 12), wraplength=380
        )
        game_details.pack(pady=20)

root = tk.Tk()
app = GameCatalogApp(root)

root.mainloop()