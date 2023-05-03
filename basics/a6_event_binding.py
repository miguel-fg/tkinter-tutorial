import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry("600x500")
window.title("Event Binding")

# widgets
text = tk.Text(master=window)
text.pack()

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="A button")
button.pack()

# events
"""
The event function is always called like:

    bind(event, function)

1. The event object must be in the correct format:

    modifier-type-detail, enclosed by <>, and always a string
    
2. The function can be done with a lambda function but it is important to PASS the event object to it

    lambda event: ----

    OR

    def function(event):
        ----

"""
window.bind("<Alt-KeyPress-a>", lambda event: print(f"an event happened: {event}"))

# text.bind("<Motion>", lambda event: print(f"x: {event.x}, y: {event.y}"))

# window.bind("<KeyPress>", lambda event: print(f"a button was pressed: {event.char}"))

entry.bind("<FocusIn>", lambda event: print("entry field was selected"))
entry.bind("<FocusOut>", lambda event: print("entry field was unselected"))

# EXERCISE:
# Print "Mousewheel" when the user holds down shift and uses the mousewheel while text is selected
text.bind("<Shift-MouseWheel>", lambda event: print("Mousewheel"))

# run
window.mainloop()
