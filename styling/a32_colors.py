import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Colors")
window.geometry("400x300")

# widgets
ttk.Label(master=window, background="red").pack(expand=True, fill="both")
ttk.Label(master=window, background="#0088FF").pack(expand=True, fill="both")
ttk.Label(master=window, background="#00FF00").pack(expand=True, fill="both")

# EXERCISE:
# Create a brownish color using hex values
ttk.Label(master=window, background="#402b06").pack(expand=True, fill="both")

# run
window.mainloop()
