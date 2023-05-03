import tkinter as tk
from tkinter import ttk

# window
window = tk.Tk()
window.title("Combining layout methods")
window.geometry("600x600")
window.minsize(600, 600)

# window widgets
menu_frame = ttk.Frame(master=window)
main_frame = ttk.Frame(master=window)

# window layout
menu_frame.place(x=0, y=0, relwidth=0.3, relheight=1)
main_frame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)


# ----------------------------menu-------------------------------------

# menu widgets
menu_button1 = ttk.Button(master=menu_frame, text="Button 1")
menu_button2 = ttk.Button(master=menu_frame, text="Button 2")
menu_button3 = ttk.Button(master=menu_frame, text="Button 3")

menu_slider1 = ttk.Scale(master=menu_frame, orient="vertical")
menu_slider2 = ttk.Scale(master=menu_frame, orient="vertical")

toggle_frame = ttk.Frame(master=menu_frame)
menu_toggle1 = ttk.Checkbutton(master=toggle_frame, text="check 1")
menu_toggle2 = ttk.Checkbutton(master=toggle_frame, text="check 2")
entry = ttk.Entry(master=menu_frame)

# menu layout
menu_frame.columnconfigure((0, 1, 2), weight=1, uniform="a")
menu_frame.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

menu_button1.grid(row=0, column=0, sticky="nsew", columnspan=2)
menu_button2.grid(row=0, column=2, sticky="nsew")
menu_button3.grid(row=1, column=0, sticky="nsew", columnspan=3)

menu_slider1.grid(row=2, column=0, rowspan=2, sticky="nsew", pady=20)
menu_slider2.grid(row=2, column=2, rowspan=2, sticky="nsew", pady=20)

# toggle layout
toggle_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")
menu_toggle1.pack(side="left", expand=True)
menu_toggle2.pack(side="left", expand=True)

# entry layout
entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")


# ----------------------------main-------------------------------------

# main widgets
entry_frame1 = ttk.Frame(master=main_frame)
main_label1 = ttk.Label(master=entry_frame1, text="label 1", background="red")
main_button1 = ttk.Button(master=entry_frame1, text="Button 1")

entry_frame2 = ttk.Frame(master=main_frame)
main_label2 = ttk.Label(master=entry_frame2, text="label 2", background="blue")
main_button2 = ttk.Button(master=entry_frame2, text="Button 2")

# main layout
entry_frame1.pack(side="left", expand=True, fill="both", padx=20, pady=20)
entry_frame2.pack(side="left", expand=True, fill="both", padx=20, pady=20)

main_label1.pack(expand=True, fill="both")
main_button1.pack(expand=True, fill="both", pady=10)

main_label2.pack(expand=True, fill="both")
main_button2.pack(expand=True, fill="both", pady=10)

# run
window.mainloop()