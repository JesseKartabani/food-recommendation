import csv
import tkinter as tk
from tkinter import Button, ttk

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --

def enter_button():
    """Writes user_input to food.csv"""
    food = user_entry.get()

root = tk.Tk()
root.geometry("400x300")
root.title("Food Recommendations")

# static label 
label = ttk.Label(root, padding=10, text="Enter your favourite meals one at a time", wraplength=200)
label.config(font=("Times New Roman",18))
label.pack()

# widget allows user to input foods
user_entry = tk.Entry (root)
user_entry.pack(pady=10)

# button calls enter_button on click
entry_button = Button(root, text="Enter", command=enter_button)
entry_button.place(x=300, y=82)



root.mainloop()