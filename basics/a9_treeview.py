import tkinter as tk
from tkinter import ttk
from random import choice  # used to pick an element from the list

# setup
window = tk.Tk()
window.geometry("600x400")
window.title("Treeview")

# data
first_names = [
    "Bob",
    "Maria",
    "Alex",
    "James",
    "Susan",
    "Henry",
    "Lisa",
    "Anna",
    "Lisa",
]
last_names = [
    "Smith",
    "Brown",
    "Wilson",
    "Thomson",
    "Cook",
    "Taylor",
    "Walker",
    "Clark",
]

emails = ["gmail", "outlook", "yahoo", "hotmail", "msn"]

# treeview
table = ttk.Treeview(master=window, columns=("first", "last", "email"), show="headings")
table.heading("first", text="First name")
table.heading("last", text="Last name")
table.heading("email", text="E-mail")

table.pack(fill="both", expand=True)

# insert values into a table
"""
Can be done manually as:

    table.insert(parent="", index=0, values=("John", "Doe", "JohnDoe@gmail.com"))
"""

for i in range(100):
    first_choice = choice(first_names)
    last_choice = choice(last_names)
    email_choice = choice(emails)

    table.insert(
        parent="",
        index=tk.END,
        values=(
            first_choice,
            last_choice,
            f"{first_choice}{last_choice}@{email_choice}.com",
        ),
    )

# events


def item_select(_):
    print(table.selection())

    for i in table.selection():
        print(table.item(i)["values"])


def delete_items(_):
    for i in table.selection():
        table.delete(i)


table.bind("<<TreeviewSelect>>", item_select)
table.bind("<Delete>", delete_items)

# run
window.mainloop()
