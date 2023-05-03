import tkinter as tk
from tkinter import ttk


def button_function():
    print("a button was pressed")


def hello_function():
    print("hello")


# create a window
window = tk.Tk()
window.title("Window and Widgets")
window.geometry("800x500")

# ttk label
label = ttk.Label(master=window, text="This is a test")
label.pack()

# tk text
text = tk.Text(master=window)
text.pack()

# ttk entry
entry = ttk.Entry(master=window)
entry.pack()

# EXERCISE: Add a text label that says "my label" and place it between the entry widget and the button
label2 = ttk.Label(master=window, text="my label")
label2.pack()

# ttk button
# don't call the function, just pass the reference
button = ttk.Button(master=window, text="A button", command=button_function)
button.pack()

# EXERCISE: Create a new button that prints "hello" when pressed
#button2 = ttk.Button(master=window, text="Exercise button", command=hello_function)
button2 = ttk.Button(master=window, text="Exercise button", command= lambda: print("hello")) #the function can also be a lambda expression
button2.pack()

# run
window.mainloop()
