import customtkinter as ctk

# EXERCISE
# Convert the following lesson 24 app to a Customtkinter app


# class that inherits from tk.Tk that functions the same way as the window methods
class App(ctk.CTk):
    def __init__(self, title: str, dimensions: tuple):
        # main setup
        super().__init__()
        self.title(title)
        self.minsize(dimensions[0], dimensions[1])
        self.geometry(f"{dimensions[0]}x{dimensions[1]}")

        # widgets
        self.menu = Menu(self)
        self.main = Main(self)

        # run
        self.mainloop()


class Menu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.place(x=0, y=0, relwidth=0.3, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        # defining widgets
        menu_button1 = ctk.CTkButton(master=self, text="button 1")
        menu_button2 = ctk.CTkButton(master=self, text="button 2")
        menu_button3 = ctk.CTkButton(master=self, text="button 3")

        menu_slider1 = ctk.CTkSlider(master=self, orientation="vertical", width=20)
        menu_slider2 = ctk.CTkSlider(master=self, orientation="vertical", width=20)

        toggleFrame = ctk.CTkFrame(master=self)
        menu_toggle1 = ctk.CTkCheckBox(master=toggleFrame, text="check 1")
        menu_toggle2 = ctk.CTkCheckBox(master=toggleFrame, text="check 2")
        entry = ctk.CTkEntry(master=self)

        # menu layout
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        menu_button1.grid(row=0, column=0, sticky="nsew", columnspan=2, padx=4, pady=4)
        menu_button2.grid(row=0, column=2, sticky="nsew", padx=4, pady=4)
        menu_button3.grid(row=1, column=0, sticky="nsew", columnspan=3, padx=4, pady=4)

        menu_slider1.grid(row=2, column=0, rowspan=2, sticky="ns", pady=20)
        menu_slider2.grid(row=2, column=2, rowspan=2, sticky="ns", pady=20)

        # toggle layout
        toggleFrame.grid(row=4, column=0, columnspan=3, sticky="nsew")
        menu_toggle1.pack(side="left", expand=True, pady=10)
        menu_toggle2.pack(side="left", expand=True, pady=10)

        # entry layout
        entry.place(relx=0.5, rely=0.95, relwidth=0.9, anchor="center")


class Main(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)

        self.entry1 = Entry(self, "label 1", "button 1", "red")
        self.entry2 = Entry(self, "label 2", "button 2", "blue")


class Entry(ctk.CTkFrame):
    def __init__(self, parent, label_text, button_text, label_background):
        super().__init__(master=parent)

        self.label = ctk.CTkLabel(
            master=self, text=label_text, bg_color=label_background
        )
        self.button = ctk.CTkButton(master=self, text=button_text)

        self.label.pack(expand=True, fill="both")
        self.button.pack(expand=True, fill="both", pady=10)

        self.pack(side="left", expand=True, fill="both", padx=20, pady=20)


# instance of the app
App("CustomTkinter application", (700, 600))
