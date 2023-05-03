import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry("600x400")
window.title("Tabs")

# Notebook widget
notebook = ttk.Notebook(master=window)

tab1 = ttk.Frame(master=notebook)
label1 = ttk.Label(master=tab1, text="Text in tab 1")
label1.pack()
button1 = ttk.Button(master=tab1, text="Button in tab 1")
button1.pack()

tab2 = ttk.Frame(master=notebook)
label2 = ttk.Label(master=tab2, text="Text in tab 2")
label2.pack()
entry2 = ttk.Entry(master=tab2)
entry2.pack()

notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

# EXERCISE
# Add another tab with 2 buttons and 1 label inside

tab3 = ttk.Frame(master=notebook)
button2 = ttk.Button(master=tab3, text="Button in tab 3")
button2.pack()
button3 = ttk.Button(master=tab3, text="Another button in tab 3")
button3.pack()
label3 = ttk.Label(master=tab3, text="Text in tab 3")
label3.pack()

notebook.add(tab3, text="Tab 3")

notebook.pack()

# run
window.mainloop()
