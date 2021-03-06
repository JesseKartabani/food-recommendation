import random
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


def clear_label(widget):
    """ Destorys widget """

    widget.destroy()


def enter_button():
    """ Appends user_input to food.csv """

    food = user_entry.get()

    if food != "":
        with open('food.csv', 'a') as f:
            w = csv.writer(f, dialect=csv)
            w.writerow([food])
            user_entry.delete(0, 10)


def guess_food():
    """ Prints a randomly selected index in food.csv """

    with open('food.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        label1 = ttk.Label(root, padding=10, text=chosen_row)
        label1.configure(background='#ADD8E6')
        label1.pack()
        # run clear_label after 2000ms (2s)
        root.after(2000, clear_label, label1)


def clear_csv():
    """ Clears the contents of food.csv """

    f = open("food.csv", "w")
    f.truncate()
    f.close()


if __name__ == "__main__":

    root = tk.Tk()
    # set window size
    root.geometry("400x300")
    # set minimum window size value
    root.minsize(400, 300)
    # set maximum window size value
    root.maxsize(400, 300)
    # set window background color
    root.configure(bg='#ADD8E6')
    # set window title
    root.title("Food Recommendations")

    # static label
    label = ttk.Label(root, padding=10, text="Enter your favourite meals one at a time")
    label.config(font=("Times New Roman", 18), background='#ADD8E6', wraplength=200)
    label.pack()

    # widget allows user to input foods
    user_entry = tk.Entry(root)
    user_entry.pack(pady=10)

    # displays Enter button
    # 1. button calls enter_button on click
    entry_button = Button(root, text="Enter", command=enter_button)
    entry_button.config(bg="#00bd56", fg="white", bd=0)
    entry_button.place(x=300, y=82)

    # displays Pick a food as a button
    # 1. button calls guess_food on click
    pick_food = Button(root, text="Pick a food", command=guess_food)
    pick_food.config(bg="#1089ff", fg="white", bd=0)
    pick_food.pack(pady=20)

    # displays Reset button
    # 1. button calls clear_csv on click
    reset_button = Button(root, text="Reset", command=clear_csv)
    reset_button.config(bg="#ed3833", fg="white", bd=0)
    reset_button.place(x=300, y=120)

    root.mainloop()
