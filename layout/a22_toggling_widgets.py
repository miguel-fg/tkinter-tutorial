import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Toggling widgets")
window.geometry("600x400")


# place
""" def toggle_label_place():
    global label_visible

    if label_visible:
        label.place_forget()
        label_visible = False
    else:
        label_visible = True
        label.place(relx=0.5, rely=0.5, anchor="center")


button = ttk.Button(master=window, text="Toggle label", command=toggle_label_place)
button.place(x=10, y=10)

label_visible = True
label = ttk.Label(master=window, text="A label")
label.place(relx=0.5, rely=0.5, anchor="center") """


# grid
""" def toggle_label_grid():
    global label_visible

    if label_visible:
        label_visible = False
        label.grid_forget()
    else:
        label_visible = True
        label.grid(column=1, row=0)


window.columnconfigure((0, 1), weight=1, uniform="a")
window.rowconfigure(0, weight=1, uniform="a")

button = ttk.Button(master=window, text="Toggle label", command=toggle_label_grid)
button.grid(column=0, row=0)

label_visible = True
label = ttk.Label(master=window, text="A label")
label.grid(column=1, row=0) """

# pack
# In this case, the behavior is different because the pack() method is influenced by other widgets and not by a position on the screen
# If pack_forget() is used as is, the button will move to the top of the window
# a frame or label without text should be used to cover the widget instead


def toggle_label_pack():
    global label_visible

    if label_visible:
        label_visible = False
        label.pack_forget()
        frame.pack(expand=True, before=button)
    else:
        label_visible = True
        frame.pack_forget()
        label.pack(expand=True, before=button)


label_visible = True
label = ttk.Label(master=window, text="A label")
label.pack(expand=True)

frame = ttk.Frame(master=window)  # widget to cover the label

button = ttk.Button(master=window, text="Toggle label", command=toggle_label_pack)
button.pack()

# run
window.mainloop()
