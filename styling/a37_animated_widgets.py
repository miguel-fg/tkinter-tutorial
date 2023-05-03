import customtkinter as ctk
from random import choice


# animated side panel
class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # general attributes
        self.start_pos = start_pos
        self.end_pos = end_pos - 0.01

        self.width = abs(start_pos - end_pos)

        # animation logic
        self.pos = start_pos
        self.in_start_pos = True

        # layout
        self.place(relx=start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    # check which way to animate
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    # calls the function up to the defined end position
    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    # moves the panel back
    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True


def move_btn():
    global button_x
    button_x += 0.05
    button.place(relx=button_x, rely=0.5, anchor="center")

    # configure
    colors = ["red", "yellow", "pink", "green", "blue", "black", "white"]
    color = choice(colors)
    button.configure(fg_color=color)


def infinite_print():
    global button_x
    button_x += 0.5
    if button_x < 10:
        print(button_x)
        print("infinite")
        window.after(10, infinite_print)


# EXERCISE:
# Combine the functions to animate the button and move it to the right side of the window
def animate_btn():
    global button_x
    button_x += 0.001
    button.place(relx=button_x, rely=0.5, anchor="se")

    if button_x < 1:
        window.after(1, animate_btn)


# window
window = ctk.CTk()
window.title("Animated Widgets")
window.geometry("600x400")

# animated panel
panel = SlidePanel(window, 1, 0.7)

# panel widgets
ctk.CTkLabel(master=panel, text="Label 1").pack(
    expand=True, fill="both", padx=2, pady=10
)
ctk.CTkLabel(master=panel, text="Label 2").pack(
    expand=True, fill="both", padx=2, pady=10
)
ctk.CTkButton(master=panel, text="Button 2").pack(
    expand=True, fill="both", padx=2, pady=10
)
ctk.CTkTextbox(master=panel, fg_color=("#dbdbdb", "#2b2b2b")).pack(
    expand=True, fill="both", pady=10
)

# button_x
button_x = 0.5

button = ctk.CTkButton(master=window, text="toggle sidebar", command=panel.animate)
button.place(relx=button_x, rely=0.5, anchor="center")


# run
window.mainloop()
