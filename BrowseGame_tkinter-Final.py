import tkinter as tk
from PIL import ImageTk, Image
import requests
from typing import List

root = tk.Tk()
root.title("Epic Game Store")
root.iconbitmap("epic_games_logo_icon_145306.ico")
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

class GamePagination:
    def __init__(self, items: List[Game], total: int):
        self.items = items
        self.total = total

class GameStoreGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.search_label = tk.Label(self, text="Games Today", font=("Trebuchet MS", 24, "bold"))
        self.search_label.grid(row=1, column=0, pady=(20, 10))

        self.search_entry = tk.Entry(self, width=60, font=("Trebuchet MS", 14))
        self.search_entry.grid(row=1, column=1, padx=(20, 30), pady=(20, 10))

        self.search_button = tk.Button(self, text="Search", command=self.search_games, font=("Trebuchet MS", 11, "bold"))
        self.search_button.grid(row=1, column=2, padx=(10, 20), pady=(20, 10))


        self.games_listbox = tk.Listbox(self, height=20, width=40, font=("Open Sans", 13))
        self.games_listbox.grid(row=2, column=0, padx=10, pady=10, rowspan=5)

        # Fetch games and insert their names into the listbox
        games = fetch_games()
        for game in games:
            self.games_listbox.insert(tk.END, game.name)

        # Bind the listbox to a mouse click event to show game details
        self.games_listbox.bind('<<ListboxSelect>>', lambda e: self.show_game_details(games))
        
        self.games_details_frame = tk.Frame(self, bd=1, relief=tk.SUNKEN)
        self.games_details_frame.grid(row=2, column=1, padx=10, pady=10, rowspan=5, sticky="n")

        self.game_details_canvas = tk.Canvas(self.games_details_frame, bd=0, highlightthickness=0, bg="white")
        self.game_details_canvas.pack(side="left", fill="both", expand=True)

        self.game_details_scrollbar = tk.Scrollbar(self.games_details_frame, orient="vertical", command=self.game_details_canvas.yview)
        self.game_details_scrollbar.pack(side="right", fill="y")

        self.game_details_canvas.configure(yscrollcommand=self.game_details_scrollbar.set)
        self.game_details_canvas.bind('<Configure>', lambda e: self.game_details_canvas.configure(scrollregion=self.game_details_canvas.bbox("all")))

    def search_games(self):
        self.games_listbox.delete(0, tk.END)
        games = fetch_games()
        search_query = self.search_entry.get().lower()
        matching_games = [game for game in games if search_query in game.name.lower()]
        for game in matching_games:
            self.games_listbox.insert(tk.END, game.name)
        self.games_listbox.bind('<<ListboxSelect>>', lambda e: self.show_game_details(matching_games))

    def show_game_details(self, games: List[Game]):
        # Clear the game details frame
        for widget in self.games_details_frame.winfo_children():
            widget.destroy()

        selected_game_index = self.games_listbox.curselection()[0]
        selected_game = games[selected_game_index]

        # Load the game image from the URL
        game_image = Image.open(requests.get(selected_game.image_url, stream=True).raw)
        game_image = game_image.resize((480, 270), Image.ANTIALIAS)
        game_image = ImageTk.PhotoImage(game_image)

        # Use a label widget to display the game image
        image_label = tk.Label(self.games_details_frame, image=game_image)
        image_label.image = game_image
        image_label.pack(side="top", padx=10, pady=10)

        # Set the font size and style for game name, price, and details
        name_font = ("Open Sans", 32, "bold")
        price_font = ("Open Sans", 24, "bold")
        details_font = ("Open Sans", 16)

        # Use a label widget to display the game details
        game_details = tk.Label(self.games_details_frame, font=name_font, text=selected_game.name)
        game_details.pack(side="top", padx=10, pady=5)

        price_label = tk.Label(self.games_details_frame, font=price_font, text=f"Price: {selected_game.price}")
        price_label.pack(side="top", padx=10, pady=3)

        details_label = tk.Label(self.games_details_frame, font=details_font, text=selected_game.details, wraplength=500)
        details_label.pack(side="top", padx=10, pady=3)

        # Bind the game details to a mouse click event
        self.games_listbox.bind('<<ListboxSelect>>', lambda e: self.show_game_details(games))


def fetch_games() -> List[Game]:
    response = requests.get("http://127.0.0.1:8000/games")
    games_data = response.json()
    games = []
    for game_data in games_data:
        game = Game(name=game_data["name"], price=game_data["price"], details=game_data["details"], image_url=game_data["image_url"])
        games.append(game)
    return games

root.iconbitmap('epic_games_logo_icon_145306.ico')
app = GameStoreGUI(master=root)
app.mainloop()