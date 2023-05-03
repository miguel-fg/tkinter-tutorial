import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry("600x400")
window.title("Menus")

# menu
menu = tk.Menu(master=window)

# sub menu
file_menu = tk.Menu(master=menu, tearoff=False)
file_menu.add_command(label="New", command=lambda: print("New file"))
file_menu.add_command(label="Open", command=lambda: print("Open file"))
file_menu.add_separator()

# another sub menu
help_menu = tk.Menu(master=menu, tearoff=False)
help_menu.add_command(
    label="Help entry", command=lambda: print(help_check_string.get())
)

help_check_string = tk.StringVar()
help_menu.add_checkbutton(
    label="check", onvalue="on", offvalue="off", variable=help_check_string
)

# menu button
menu_button = ttk.Menubutton(master=window, text="Menu Button")
menu_button.pack()

button_sub_menu = tk.Menu(master=menu_button, tearoff=False)
button_sub_menu.add_command(label="Entry 1", command=lambda: print("test 1"))
button_sub_menu.add_checkbutton(label="Check 1")

menu_button.configure(menu=button_sub_menu)

"""
it is possible to use 

    menu_button["menu"] = button_sub_menu

instead of .configure(menu=)
"""

# adding the submenus to the main menu
menu.add_cascade(label="File", menu=file_menu)
menu.add_cascade(label="Help", menu=help_menu)


# EXERCISE:
# add another menu to the main menu, it should have its own sub menu
exercise_menu = tk.Menu(master=menu, tearoff=False)
menu.add_cascade(label="Exercise", menu=exercise_menu)

exercise_menu.add_command(label="option 1", command=lambda: print("option 1"))

exercise_sub_menu = tk.Menu(master=exercise_menu, tearoff=False)
exercise_menu.add_cascade(label="more options", menu=exercise_sub_menu)

exercise_sub_menu.add_command(label="sub option 1", command=lambda: print("INCEPTION"))
exercise_sub_menu.add_checkbutton(label="hi")

window.configure(menu=menu)  # instead of pack()


# run
window.mainloop()
