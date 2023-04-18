import tkinter as tk
import requests

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
            master, text=game.name, font=("Trebuchet MS", 14), width=20, height=2, command=command
        )
        self.game = game
        self.grid(row=row, column=column, padx=10, pady=10)
class GameCatalogApp:
    def __init__(self, master, game_list):
        self.master = master
        self.master.title("Epic Game Store")
        self.game_list = game_list

        self.label = tk.Label(
            self.master, text="Browse Game", font=("Trebuchet MS", 24, "bold")
        )
        self.label.grid(row=0, column=0)

        self.buttons_frame = tk.Frame(self.master)
        self.buttons_frame.grid(row=1, column=0, pady=20, sticky="nsew")

        self.buttons = []
        for i, game in enumerate(self.game_list):
            column = i % 3
            row = i // 3
            button = GameButton(
                self.buttons_frame, game, row, column, lambda game=game: self.show_game_info(game)
            )
            self.buttons.append(button)
       # Add empty frames to fill up the last row if there are not enough buttons to fill up all 3 columns
        if len(self.game_list) % 3 != 0:
            for i in range(3 - (len(self.game_list) % 3)):
                empty_frame = tk.Frame(self.buttons_frame)
                empty_frame.grid(row=len(self.game_list) // 3, column=i)

    def show_game_info(self, game):
        # Make a request to the backend to retrieve more information about the game
        response = requests.get(f"http://10.62.8.243:8000/")
        data = response.json()
        
        details_window = tk.Toplevel(self.master)
        details_window.title(game.name)
        details_window.geometry("400x300")
        
        game_name = tk.Label(
            details_window, text=game.name.upper(), font=("Arial", 16, "bold")
        )
        game_name.pack(pady=(20, 10))
        
        game_price = tk.Label(
            details_window, text=f"Price: {game.price} Baht", font=("Arial", 12)
        )
        game_price.pack()
        
        game_details = tk.Label(
            details_window, text=data["description"], font=("Arial", 12), wraplength=380
        )
        game_details.pack(pady=20)

root = tk.Tk()

# Example usage:
game1 = Game("GTA V", 1850, "Open-world action-adventure game.")
game2 = Game("Minecraft", 790, "Sandbox game where you can build and explore.")
game3 = Game("Fortnite", 0, "A FREE Battle royale game with cartoon graphics.")
game4 = Game('Hogwart', 1500, 'Single-player Action-adventure game')
game5 = Game('Skyrim', 1400, 'Single-player Action game')
game6 = Game('Destiny', 900, 'Multi-player FPS game')
game7 = Game('Fall Guys', 500, 'A battle royale game')
game8 = Game('Among Us', 120, 'A multiplayer game where you work together to find the imposter on a spaceship')
game9 = Game('Valheim', 280, 'A Viking-themed survival game where you explore and build in a procedurally generated world')
game10 = Game('Phasmophobia', 350, 'A horror game where you and your team investigate haunted locations and try to capture evidence of ghosts')

game_list = [game1, game2, game3, game4, game5, game6, game7, game8, game9, game10]
app = GameCatalogApp(root, game_list)

# Start the Tkinter event loop
root.mainloop()