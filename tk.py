import requests
import tkinter as tk

window = tk.Tk()
window.title("My App")
window.geometry("400x400")

def get_data():
    response = requests.get("http://127.0.0.1:8000")
    data = response.json()
    label.config(text=data)

label = tk.Label(window, text="")
label.pack()
button = tk.Button(window, text="Get Data", command=get_data)
button.pack()
window.mainloop()
