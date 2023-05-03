import tkinter as tk
from tkinter import ttk

"""
IMPORTANT NOTES:

    label = ttk.Label(master=window, text="A label", width=50).pack(fill="x")

    1. the specified width of the label is NOT in pixels, it's in number of characters
    2. the width used by pack() will ALWAYS override whatever widget width is set
        99% of the time, you want to use layout methods instead of hardcoded numbers to set sizes
"""

# window
window = tk.Tk()
window.title("Understanding widget sizes")
window.geometry("400x300")

# widgets
label1 = ttk.Label(master=window, text="Label 1", background="green")  # reference label
label2 = ttk.Label(master=window, text="Label 2", background="red", width=50)

# layout
# label1.pack()
# label2.pack(fill="x")

# grid
window.columnconfigure((0, 1), weight=1, uniform="a")
window.rowconfigure((0, 1), weight=1, uniform="a")

label1.grid(row=0, column=0)
label2.grid(
    row=1, column=0, sticky="nsew"
)  # the in-built layout method will also override the label size

# run
window.mainloop()
