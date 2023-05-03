import tkinter as tk
from tkinter import ttk


def button_func():
    # get the content of the entry
    # IMPORTANT: Most widgets DO NOT have  a get() function
    entry_text = entry.get()

    # update the label
    label["text"] = entry_text

    """
    label.config(text="some other text")
    label.configure(text="some other text")
    
    both are equivalent with the method above, but they're not as concise and will be deprecated in the near future
    """

    entry["state"] = "disabled"

    """
    if you run 
        print(<WIDGET>.configure)
    
    you will find a list of all available parameters that can be changed for that <WIDGET>
    
    """


def other_button_func():
    label["text"] = "some text"
    entry["state"] = "enabled"


# window
window = tk.Tk()
window.title("Getting and Setting widgets")

# widgets
label = ttk.Label(master=window, text="some text")
label.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="the button", command=button_func)
button.pack()

# EXERCISE: add another button that changes text back to "some text" and enables the entry again
button2 = ttk.Button(master=window, text="the other button", command=other_button_func)
button2.pack()

# run
window.mainloop()
