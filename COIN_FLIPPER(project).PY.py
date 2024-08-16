import tkinter as tk
import ttkbootstrap as ttk
from PIL import ImageTk, Image
import random
import customtkinter

def coin_flip():
    outcomes = ("head.png", "tail.png")
    result = random.choice(outcomes)
    result_image = ImageTk.PhotoImage(Image.open(result))
    result_label.config(image=result_image)
    result_label.image = result_image

app = tk.Tk()
app.title("Coin-Flipper")
style= ttk.Style(theme="flatly")

headImg = ImageTk.PhotoImage(Image.open("head.png"))
tailImg = ImageTk.PhotoImage(Image.open("tail.png"))

# btn = CTkButton(master=app, text="Click Me", command=coin_flip, corner_radius=32, fg_color="#C850C0",
#                 hover_color="#4158D0",border_color="#FFCC70",border_width=2)
# btn.place(relx=0.5, rely=0.5, anchor="center")
button = ttk.Button(text="Flip Coin", command=coin_flip, style="primary.TButton")
result_label = ttk.Label(image=headImg)
button.pack(pady=10)
result_label.pack(pady=10)

app.mainloop()