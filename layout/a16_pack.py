import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.geometry("400x600")
window.title("Pack")

# widgets
label1 = ttk.Label(master=window, text="First Label", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue")
label3 = ttk.Label(master=window, text="Last of the labels", background="green")
button = ttk.Button(master=window, text="Button")

# layout
label1.pack(side="top", expand=True, fill="both", pady=10, padx=10)
label2.pack(side="left", expand=True, fill="both")
label3.pack(side="top", expand=True, fill="both")
button.pack(side="top", expand=True, fill="both")

# run
window.mainloop()
