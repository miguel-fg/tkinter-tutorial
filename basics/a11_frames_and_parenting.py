import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry("600x400")
window.title("Frames & Parenting")

# frame
frame = ttk.Frame(
    master=window, width=200, height=200, borderwidth=10, relief=tk.GROOVE
)
frame.pack_propagate(False)  # prevents children from overriding size values
frame.pack(side="left")

# parenting
label = ttk.Label(master=frame, text="Label in frame")
label.pack()

button = ttk.Button(master=frame, text="Button in a frame")
button.pack()

# EXAMPLE
label2 = ttk.Label(window, text="Label outside frame")
label2.pack(side="left")

"""
EXERCISE:
create another frame with a label, a button and an entry
place it to the right of the other widgets

"""

frame2 = ttk.Frame(
    master=window, width=150, height=150, borderwidth=10, relief=tk.GROOVE
)
frame2.pack_propagate(False)
frame2.pack(side="right")

label3 = ttk.Label(master=frame2, text="Exercise label")
label3.pack()

button2 = ttk.Button(master=frame2, text="Exercise button")
button2.pack()

entry = ttk.Entry(master=frame2)
entry.pack()

# run
window.mainloop()
