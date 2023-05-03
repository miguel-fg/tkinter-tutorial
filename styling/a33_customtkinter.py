import customtkinter as ctk

# you can combine widgets from standard tkinter as well
import tkinter as tk
from tkinter import ttk

"""
IMPORTANT NOTES:

Customtkinter uses the same ttk widgets but makes them easier to customise. (robust documentation too :))
"""


class App(ctk.CTk):
    def __init__(self, size):
        super().__init__()
        self.title("Customtkinter app")
        self.geometry(f"{size[0]}x{size[1]}")

        # widgets
        string_var = ctk.StringVar(value="a custom string")
        self.label = ctk.CTkLabel(
            master=self,
            text="A ctk label",
            fg_color=("blue", "red"),  # first color in light mode, second in dark mode
            text_color=("black", "white"),  #
            corner_radius=10,
            textvariable=string_var,
        )
        self.label.pack()

        self.button = ctk.CTkButton(
            master=self,
            text="A ctk button",
            fg_color="#FF0",
            text_color="#000",
            hover_color="#AA0",
            command=lambda: ctk.set_appearance_mode("light"),
        )
        self.button.pack()

        self.frame = ctk.CTkFrame(master=self)
        self.frame.pack()

        self.slider = ctk.CTkSlider(master=self.frame)
        self.slider.pack(padx=20, pady=20)

        # EXERCISE
        # Make a horrible switch
        self.switch = ctk.CTkSwitch(
            master=self,
            text="Exercise Switch",
            switch_height=25,
            corner_radius=2,
            switch_width=50,
            fg_color="red",
            border_color="blue",
            button_color="green",
            button_hover_color="yellow",
            progress_color="pink",
        )
        self.switch.pack()

        self.mainloop()


App((600, 400))
