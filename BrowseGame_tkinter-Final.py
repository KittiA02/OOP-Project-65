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

class GameStoreGUI(tk.Frame, tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("1458x820")
        self.master = master
        self.pack(padx=0, pady=0, expand=True, fill='both')
        self.create_widgets()

    def create_widgets(self):
        self.configure(bg="#34495E")
        
        self.search_label = tk.Label(self, text="Browse Game", font=("Trebuchet MS", 36, "bold"), fg="#ABEBC6", bg="#34495E")
        self.search_label.grid(row=1, column=0, pady=(20, 10))

        self.search_entry = tk.Entry(self, width=60, font=("Trebuchet MS", 14))
        self.search_entry.grid(row=1, rowspan=1, column=1, padx=(20, 30), pady=(20, 10))

        self.search_button = tk.Button(self, text="Search", command=self.search_games, font=("Trebuchet MS", 14, "bold"), fg="yellow", bg="#223a4c")
        self.search_button.grid(row=1, column=2, padx=(10, 20), pady=(20, 10))
        
        self.search_label = tk.Label(self, text="Browse:", font=("Trebuchet MS", 20), fg="#ABEBC6", bg="#34495E")
        self.search_label.grid(row=2, column=0, pady=(5, 2))
        
        self.checkout_button = tk.Button(self, text="Buy Now!", command=self.checkout, font=("Trebuchet MS", 14, "bold"))
        self.checkout_button.grid(row=7, column=1, padx=(10, 20), pady=(5, 10))
        
        self.cart_button = tk.Button(self, text="Add this game to my cart", command=self.add_to_cart, font=("Trebuchet MS", 14, "bold"))
        self.cart_button.grid(row=8, column=1, padx=(10, 20), pady=(5, 10))

        # Bind the Return key to the search button
        self.search_entry.bind('<Return>', lambda e: self.search_button.invoke())
        
        self.games_listbox = tk.Listbox(self, height=20, width=35, font=("Open Sans", 16, "bold"), fg="#003333", bg="#D1F2EB")
        self.games_listbox.grid(row=3, column=0, padx=10, pady=10, rowspan=5)

        # Bind the listbox to a mouse click event to show game details
        self.games_listbox.bind('<<ListboxSelect>>', lambda e: self.show_game_details(games))

        self.games_listbox_scrollbar = tk.Scrollbar(self, orient="vertical", command=self.games_listbox.yview)
        self.games_listbox_scrollbar.grid(row=2, column=1, sticky="ns")

        self.games_listbox.config(yscrollcommand=self.games_listbox_scrollbar.set)

        # Attach the scrollbar to the games_listbox widget
        self.games_listbox_scrollbar.config(command=self.games_listbox.yview)
        self.games_listbox.config(yscrollcommand=self.games_listbox_scrollbar.set)

        # Set the scrollbar to fill the available vertical space
        self.games_listbox_scrollbar.grid(row=2, column=0, sticky="ne")

        # Fetch games and insert their names into the listbox
        games = fetch_games()
        for game in games:
            self.games_listbox.insert(tk.END, game.name)

        # Bind the listbox to a mouse click event to show game details
        self.games_listbox.bind('<<ListboxSelect>>', lambda e: self.show_game_details(games))
        
        self.games_details_frame = tk.Frame(self, bd=1, relief=tk.SUNKEN, highlightthickness=0)
        self.games_details_frame.configure(bg="#34495E")
        self.games_details_frame.grid(row=2, column=1, columnspan=2, padx=10, pady=10, rowspan=5, sticky="n")

        self.game_details_canvas = tk.Canvas(self.games_details_frame, bd=0, highlightthickness=0)
        self.game_details_canvas.configure(bg="#34495E")
        self.game_details_canvas.pack(side="left", fill="both", expand=True)
        self.game_details_canvas.bind('<Configure>', lambda e: self.game_details_canvas.configure(scrollregion=self.game_details_canvas.bbox("all")))


    def search_games(self):
        query = self.search_entry.get()
        self.search_label['text'] = f"Results for '{query}'"
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
        
        if (selected_game.price == 0):
            selected_game.price = "Free"

        # Load the game image from the URL
        game_image = Image.open(requests.get(selected_game.image_url, stream=True).raw)
        game_image = game_image.resize((480, 270), Image.ANTIALIAS)
        game_image = ImageTk.PhotoImage(game_image)

        # Use a label widget to display the game image
        image_label = tk.Label(self.games_details_frame, image=game_image)
        image_label.image = game_image
        image_label.pack(side="top", padx=10, pady=10)

        # Set the font size and style for game name, price, and details
        name_font = ("Trebuchet MS", 32, "bold")
        details_font = ("Open Sans", 14)

        # Use a label widget to display the game details
        game_details = tk.Label(self.games_details_frame, font=name_font, text=selected_game.name, fg="#F0B27A", bg="#34495E")
        game_details.pack(side="top", padx=10, pady=2)

        price_label = tk.Label(self.games_details_frame, font=("Trebuchet MS", 21, "bold"), text=f"Price: {selected_game.price}", fg="#F0B27A", bg="#34495E")
        price_label.pack(side="top", padx=10, pady=0)

        details_label = tk.Label(self.games_details_frame, font=details_font, text=selected_game.details, wraplength=500, fg="#F0B27A", bg="#34495E")
        details_label.pack(side="top", padx=10, pady=3)

        # Bind the game details to a mouse click event
        self.games_listbox.bind('<<ListboxSelect>>', lambda e: self.show_game_details(games))
        
    def add_to_cart(self):
        pass
        
    def checkout(self):
        pass
        

def fetch_games() -> List[Game]:
    response = requests.get("http://127.0.0.1:8000/games")
    games_data = response.json()
    games = []
    for product in games_data:
        name = product['name']
        price = product['price']
        details = product['details']
        image_url = product['image_url']
        games.append(Game(name, price, details, image_url))
    games.sort(key=lambda x: x.name)
    return games

root.iconbitmap('epic_games_logo_icon_145306.ico')

app = GameStoreGUI(master=root)
app.mainloop()