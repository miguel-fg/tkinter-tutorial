import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x400")
window.title("Combobox & Spinbox")

# combobox
items = ["Ice cream", "Pizza", "Broccoli"]  # drop down menu items
food_string = tk.StringVar(value=items[0])  # value on startup

combobox = ttk.Combobox(master=window, textvariable=food_string)
combobox["values"] = items  # rest of the items are assigned to the combobox
combobox.pack()

# events

combobox.bind(
    "<<ComboboxSelected>>",
    lambda event: combo_label.config(text=f"Selected value: {food_string.get()}"),
)

combo_label = ttk.Label(master=window, text="label")
combo_label.pack()

# spinbox
spin_int = tk.IntVar(value=12)

spinbox = ttk.Spinbox(
    master=window,
    from_=3,
    to=20,
    increment=3,
    command=lambda: print(spin_int.get()),
    textvariable=spin_int,
)
# OR spinbox["value"] = [1,2,3,4,5]
spinbox.pack()

# events

spinbox.bind("<<Increment>>", lambda event: print("up"))
spinbox.bind("<<Decrement>>", lambda event: print("down"))

#EXERCISE:
# Create a spinbox that contains the letters A B C D E
# and print the value whenever the value is decreased

e_spin_items = ['A', 'B', 'C', 'D', 'E']
e_spin_val = tk.StringVar(value=e_spin_items[0])

e_spin = ttk.Spinbox(master=window, textvariable=e_spin_val)
e_spin['value'] = e_spin_items
e_spin.pack()

e_spin.bind("<<Decrement>>", lambda event: print(e_spin_val.get()))

window.mainloop()
