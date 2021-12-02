# A simple tkinter window
import tkinter as tk
from tkinter import ttk

# -- Windows only configuration --
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
# -- End Windows only configuration --


root = tk.Tk()
root.geometry("400x300")
root.title("Food Recommendations")

# static label 
label = ttk.Label(root, padding=10, text="Enter your favourite meals")
label.config(font=("Times New Roman",20))
label.pack()

# widget allows user to input foods
user_entry = tk.Entry (root)
user_entry.pack(pady=10)

root.mainloop()