import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.title("More on the window")

# EXERCISE:
# Start the window in the middle of the screen
mid_x = window.winfo_screenwidth() // 2
mid_y = window.winfo_screenheight() // 2
window_width = 600
window_height = 400
window.geometry(
    f"{window_width}x{window_height}+{mid_x-(window_width // 2)}+{mid_y-(window_height // 2)}"
)  # widthxheight+left+top


# FILEPATH = ""
# window.iconbitmap(PATH)
# to change the icon of the window. it has to be in .ICO format

# window sizes
window.minsize(200, 100)
window.maxsize(800, 700)
# window.resizable(True, False)

# screen attributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
window.attributes("-alpha", 1)
window.attributes("-topmost", True)  # window always on top

# security event
window.bind("<Escape>", lambda e: window.quit())

# title bar
window.overrideredirect(True)  # disable the title bar
grip = ttk.Sizegrip(master=window)
grip.place(relx=1.0, rely=1.0, anchor="se")  # placement of the grip widget

# DO NOT USE THIS:
# window.attributes("-disable", True)

# run
window.mainloop()
