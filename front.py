import tkinter as tk
from tkinter import ttk
import requests

API_URL = "http://127.0.0.1:8000"

def fetch_games():
    response = requests.get(API_URL + "/")
    if response.status_code == 200:
        return response.json()
    else:
        return []

def search_game():
    search_query = {game : game_search_var.get()}
    response = requests.post(API_URL + "/search_game", json=search_query)
    if response.status_code == 200:
        result = response.json()
        if "error" not in result:
            result_label.config(text=f"Title: {result['title']}\nPrice: {result['price']}\nDescription: {result['description']}")
        else:
            result_label.config(text=result["error"])
    else:
        result_label.config(text="Error fetching game data")

# Create the main window
root = tk.Tk()
root.title("Game Catalog")
root.geometry("800x600")

# Create the game list frame
game_list_frame = ttk.Frame(root)
game_list_frame.pack(side="left", padx=10, pady=10)

game_list_label = ttk.Label(game_list_frame, text="Game List", font=("Arial", 18))
game_list_label.pack(pady=10)

game_listbox = tk.Listbox(game_list_frame, width=40, height=20)
game_listbox.pack()

games = fetch_games()
for game in games:
    game_listbox.insert(tk.END, game)

# Create the search and result frame
search_result_frame = ttk.Frame(root)
search_result_frame.pack(side="left", padx=10, pady=10)

search_label = ttk.Label(search_result_frame, text="Search Game", font=("Arial", 18))
search_label.pack(pady=10)

game_search_var = tk.StringVar()
game_search_entry = ttk.Entry(search_result_frame, textvariable=game_search_var, width=30)
game_search_entry.pack(pady=5)

search_button = ttk.Button(search_result_frame, text="Search", command=search_game)
search_button.pack(pady=5)

result_label = ttk.Label(search_result_frame, text="", font=("Arial", 14), justify=tk.LEFT)
result_label.pack(pady=10)

root.mainloop()
