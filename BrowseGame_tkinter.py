import tkinter as tk


class Game:
    def __init__(self, name, price, details):
        self.name = name
        self.price = price
        self.details = details
        
    def get_info(self):
        return f"{self.name} ({self.price} Baht) - {self.details}"


class GameButton:
    def __init__(self, master, game, row, column, app):
        self.game = game
        self.app = app
        self.button = tk.Button(master, text=self.game.name, command=self.show_info, width=10, height=2)
        self.button.grid(row=row, column=column, padx=10, pady=10)
    
    def show_info(self):
        info_window = tk.Toplevel(self.app.master)
        info_window.title(self.game.name)
        info_label = tk.Label(info_window, text=self.game.get_info())
        info_label.pack(padx=10, pady=10)


class GameCatalogApp:
    def __init__(self, master, game_list):
        self.master = master
        self.master.title("Epic Game Store")
        self.game_list = game_list
        
        self.label = tk.Label(self.master, text="Browse Game", font=("Arial", 24, "bold"))
        self.label.grid(row=0, column=0)
        
        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.grid(row=1, column=0, pady=20, sticky='nsew')
        
        self.buttons = []
        for i, game in enumerate(self.game_list):
            button = GameButton(self.buttons_frame, game, i, 0, self)
            self.buttons.append(button)

            
class GameList:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        self.games.append(game)

    def browse_games(self):
        return [game.get_info() for game in self.games]


root = tk.Tk()


# Example usage:
game1 = Game("GTA V", 1850, "Open-world action-adventure game.")
game2 = Game("Minecraft", 790, "Sandbox game where you can build and explore.")
game3 = Game("Fortnite", 0, "A FREE Battle royale game with cartoon graphics.")
game4 = Game('Hogwart', 1500, 'Single-player Action-adventure game')
game5 = Game('Skyrim', 1400, 'Single-player Action game')
game6 = Game('Destiny', 900, 'Multi-player FPS game')

game_list = [game1, game2, game3, game4, game5, game6]
app = GameCatalogApp(root, game_list)

# Start the Tkinter event loop
root.mainloop()
