import tkinter as tk
from tkinter import ttk

"""
IMPORTANT NOTES:

Widgets are always placed on top of other widgets when they are CREATED
(NOT when they are placed!)
"""

# window
window = tk.Tk()
window.title("Stacking order")
window.geometry("400x400")

# widgets
# whatever widget is created first will be at the bottom
label1 = ttk.Label(master=window, text="Label 1", background="green")
label2 = ttk.Label(master=window, text="Label 2", background="red")

"""
You can add:
    label1.lift() OR .tkraise()
    label2.lower()  

to raise and lower widgets
"""

button1 = ttk.Button(
    master=window,
    text="Raise label 1",
    command=lambda: label1.lift(
        aboveThis=label2
    ),  # by default raises widgets to the top
)
button2 = ttk.Button(master=window, text="Raise label 2", command=lambda: label2.lift())

# layout
# the order of place does not matter
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)

button1.place(rely=1, relx=0.8, anchor="se")
button2.place(rely=1, relx=1, anchor="se")

# EXERCISE
# Add a third label and button
# The command for the button should raise the third label all the way to the top

label3 = ttk.Label(master=window, text="Label 3", background="yellow")
button3 = ttk.Button(master=window, text="Raise label 3", command=lambda: label3.lift())

label3.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5, anchor="center")
button3.place(rely=1, relx=0.6, anchor="se")

# run
window.mainloop()
