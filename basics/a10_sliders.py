import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext as st  # contains other widgets

# setup
window = tk.Tk()
window.title("Sliders")

# scale
scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(
    master=window,
    command=lambda value: progress.stop(),
    from_=0,
    to=25,
    length=300,
    orient="horizontal",
    variable=scale_float,
)
scale.pack()

# progress bar
progress = ttk.Progressbar(
    master=window,
    variable=scale_float,
    maximum=25,
    orient="horizontal",
    mode="determinate",
    length=400,
)
progress.pack()

# almost never useful:
# progress.start(1000)

# Scrolledtext
scrolled_text = st.ScrolledText(master=window, width=100, height=10)
scrolled_text.pack()


"""
EXERCISE:
create a progress bar that is vertical, starts automatically and also shows the progress as a number.

There should also be a scale slider that is affected by the progress bar
"""

e_prog_val = tk.DoubleVar()
e_progress = ttk.Progressbar(
    master=window,
    variable=e_prog_val,
    orient="vertical",
)
e_progress.pack()
e_progress.start()

label = ttk.Label(master=window, textvariable=e_prog_val)
label.pack()

e_scale = ttk.Scale(master=window, from_=0, to=100, length=100, variable=e_prog_val)
e_scale.pack()

# run
window.mainloop()
