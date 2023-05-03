import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Tkinter Place")
window.geometry("400x600")

# widgets
label1 = ttk.Label(master=window, text="Label 1", background="red")
label2 = ttk.Label(master=window, text="Label 2", background="blue")
label3 = ttk.Label(master=window, text="Label 3", background="green")

button = ttk.Button(master=window, text="Button 1")

# layout
label1.place(x=300, y=100, width=100, height=200)  # absolute positioning (non-scaling)
label2.place(
    relx=0.2, rely=0.1, relwidth=0.4, relheight=0.5
)  # relative positioning (always scales)

# EXERCISE
# place label 3 in the same place as label 2 using absolute positioning
label3.place(x=400 // 5, y=600 // 10, width=400 * 2 // 5, height=600 // 2)

button.place(relx=1, rely=1, anchor="se")

# frame
frame = ttk.Frame(master=window)

frame_label = ttk.Label(master=frame, text="Frame label", background="yellow")
frame_button = ttk.Button(master=frame, text="Frame button")

# frame layout
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_button.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# EXERCISE 2
# create a label and place it right in the center of the window
# the label should be half as wide as the window and be 200px tall
e_label = ttk.Label(master=window, text="Exercise label", background="pink")
e_label.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.5, height=200)

# run
window.mainloop()
