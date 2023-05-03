import tkinter as tk
import ttkbootstrap as ttk

# using ttkbootstrap to modify a24 file 

# use python -m ttkcreator to create custom themes
class App(ttk.Window):
    def __init__(self, title: str, dimensions: tuple):
        # main setup
        super().__init__(themename="morph")
        self.title(title)
        self.minsize(dimensions[0], dimensions[1])
        self.geometry(f"{dimensions[0]}x{dimensions[1]}")

        # widgets
        self.menu = Menu(self)
        self.main = Main(self)

        # run
        self.mainloop()

class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        # defining widgets
        menu_button1 = ttk.Button(master=self, text="Button 1", bootstyle="secondary")
        menu_button2 = ttk.Button(master=self, text="Button 2", bootstyle="secondary")
        menu_button3 = ttk.Button(master=self, text="Button 3", bootstyle="secondary")

        menu_slider1 = ttk.Scale(master=self, orient="vertical")
        menu_slider2 = ttk.Scale(master=self, orient="vertical")

        toggle_frame = ttk.Frame(master=self)
        menu_toggle1 = ttk.Checkbutton(master=toggle_frame, text="check 1")
        menu_toggle2 = ttk.Checkbutton(master=toggle_frame, text="check 2")
        entry = ttk.Entry(master=self)

        # menu layout
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        menu_button1.grid(row=0, column=0, sticky="nsew", columnspan=2, padx=5, pady=5)
        menu_button2.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        menu_button3.grid(row=1, column=0, sticky="nsew", columnspan=3, padx=5, pady=5)

        menu_slider1.grid(row=2, column=0, rowspan=2, sticky="nsew", pady=20)
        menu_slider2.grid(row=2, column=2, rowspan=2, sticky="nsew", pady=20)

        # toggle layout
        toggle_frame.grid(row=4, column=0, columnspan=3, sticky="nsew")
        menu_toggle1.pack(side="left", expand=True)
        menu_toggle2.pack(side="left", expand=True)

        # entry layout
        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

        self.entry1 = Entry(self, "label 1", "Button 1", "inverse-danger")
        self.entry2 = Entry(self, "label 2", "Button 2", "inverse-info")


class Entry(ttk.Frame):
    def __init__(self, parent, label_text, button_text, label_background):
        super().__init__(master=parent)

        label = ttk.Label(master=self, text=label_text, bootstyle=label_background)
        button = ttk.Button(master=self, text=button_text, bootstyle="dark")

        label.pack(expand=True, fill="both")
        button.pack(expand=True, fill="both", pady=10)

        self.pack(side="left", expand=True, fill="both", padx=20, pady=20)


# instance of the app
App("ttkbootstrap app", (600, 600))