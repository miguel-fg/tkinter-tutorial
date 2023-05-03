import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Buttons")
window.geometry("600x400")


# basic button
def button_func():
    print("a basic button")
    print(radio_var.get())


button_string = tk.StringVar(value="a button with string var")
button = ttk.Button(master=window, command=button_func, textvariable=button_string)
button.pack()

# checkbutton
# use a tk variable to get the state of the checkbutton
check_var = tk.IntVar(value=10)
check = ttk.Checkbutton(
    master=window,
    text="checkbox 1",
    command=lambda: print(check_var.get()),
    variable=check_var,
    onvalue=10,
    offvalue=5,
)
check.pack()

# radio buttons
# always set different values for radio buttons, or they will be treated as the same
radio_var = (
    tk.StringVar()
)  # String vars are helpful if the values are not the same type as it converts everything to a String


radio1 = ttk.Radiobutton(
    master=window,
    text="Radiobutton 1",
    value="radio 1",
    variable=radio_var,
    command=lambda: print(radio_var.get()),
)
radio1.pack()
radio2 = ttk.Radiobutton(
    master=window, text="Radiobutton 2", value=2, variable=radio_var
)
radio2.pack()

"""
EXERCISE

Create another checkbutton and 2 radiobuttons

Radio buttons:
    values are A and B
    ticking either prints the value of the checkbutton
    ticking the radio button unchecks the checkbutton

Checkbutton:
    ticking the checkbutton prints the value of the radio button value
    use tkinter variable for Booleans
"""

# checkbutton
e_check_var = tk.BooleanVar()
e_check = ttk.Checkbutton(
    master=window,
    text="Exercise_checkbutton",
    variable=e_check_var,
    command=lambda: print(e_radio_var.get()),
)
e_check.pack()


# radio button functionality
def e_radio_func():
    print(e_check_var.get())
    e_check_var.set(False)


# radio buttons
e_radio_var = tk.StringVar()
e_radio1 = ttk.Radiobutton(
    master=window, text="A", value="A", variable=e_radio_var, command=e_radio_func
)
e_radio1.pack()
e_radio2 = ttk.Radiobutton(
    master=window, text="B", value="B", variable=e_radio_var, command=e_radio_func
)
e_radio2.pack()
# run
window.mainloop()
