import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("400x600")
window.title("Pack w/Frames")

# top frame
top_frame = ttk.Frame(master=window)

label1 = ttk.Label(master=top_frame, text="First label", background="red")
label2 = ttk.Label(master=top_frame, text="Label 2", background="blue")

# middle widget
label3 = ttk.Label(master=window, text="Another label", background="green")

# bottom frame
bottom_frame = ttk.Frame(master=window)

label4 = ttk.Label(master=bottom_frame, text="Last of the labels", background="orange")
button = ttk.Button(master=bottom_frame, text="A button")
button2 = ttk.Button(master=bottom_frame, text="Another button")

# top layout
label1.pack(side="left", fill="both", expand=True)
label2.pack(side="left", fill="both", expand=True)
top_frame.pack(fill="both", expand=True)

# middle layout
label3.pack(expand=True)

# bottom layout
button.pack(side="left", expand=True, fill="both")
label4.pack(side="left", expand=True, fill="both")
button2.pack(side="left", expand=True, fill="both")
bottom_frame.pack(expand=True, fill="both", padx=20, pady=20)

# EXERCISE
# Create 3 more buttons and another frame
# The fram should be on the right and inside the bottom frame
# and the buttons should be stacked vertically inside of it

# exercise widgets
e_frame = ttk.Frame(master=bottom_frame)
e_button1 = ttk.Button(master=e_frame, text="Button 3")
e_button2 = ttk.Button(master=e_frame, text="Button 4")
e_button3 = ttk.Button(master=e_frame, text="Button 5")

# exercise layout
e_button1.pack(expand=True, fill="both")
e_button2.pack(expand=True, fill="both")
e_button3.pack(expand=True, fill="both")
e_frame.pack(side="right", expand=True, fill="both")

# run
window.mainloop()
