import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

"""
Images don't scale properly by default. (Add to a canvas and resize in real time)
Images need the pillow library

IMPORTANT NOTES:
Lesson a39 is missing because i don't want to go through importing large amounts of images and my applications will not use animated images 
"""


# resize logic
def stretch_image(event):
    global resized_tk  # images should always be in the same scope as mainloop()

    # window size
    width = event.width
    height = event.height

    # create an image
    resized_image = image_original.resize(
        (width, height)
    )  # DO NOT IMPORT THE IMAGE AGAIN
    resized_tk = ImageTk.PhotoImage(resized_image)

    # place on the canvas
    canvas.create_image(0, 0, image=resized_tk, anchor="nw")


# cut off parts of the images that don't fit
def fill_image(event):
    global resized_tk

    # current ratio
    canvas_ratio = event.width / event.height

    # image coordinates
    if canvas_ratio > image_ratio:  # canvas is wider than the image
        width = int(event.width)
        height = int(width / image_ratio)
    else:  # canvas is narrower than the image
        height = int(event.height)
        width = int(height * image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    canvas.create_image(
        event.width // 2, event.height // 2, anchor="center", image=resized_tk
    )


def keep_ratio(event):
    global resized_tk

    # current ratio
    canvas_ratio = event.width / event.height

    # image coordinates
    if canvas_ratio > image_ratio:  # canvas is wider than the image
        height = int(event.height)
        width = int(height * image_ratio)
    else:  # canvas is narrower than the image
        width = int(event.width)
        height = int(width / image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)

    canvas.create_image(
        event.width // 2, event.height // 2, anchor="center", image=resized_tk
    )


# setup
window = tk.Tk()
window.geometry("600x400")
window.title("Images")

# grid layout
window.columnconfigure((0, 1, 2, 3), weight=1, uniform="a")
window.rowconfigure(0, weight=1, uniform="a")


# import an image
image_original = Image.open(".\styling\Images\Spartan3E_big.png")
image_ratio = image_original.size[0] / image_original.size[1]  # original image ratio
image_tk = ImageTk.PhotoImage(image_original)  # to make compatible with tkinter

python_logo = Image.open(".\styling\Images\Python_logo_big.png").resize((30, 30))
python_logo_tk = ImageTk.PhotoImage(python_logo)

# for ctk widgets you need to provide images for each theme
img_ctk = ctk.CTkImage(
    light_image=Image.open(".\styling\Images\Python_logo_big.png"),
    dark_image=Image.open(".\styling\Images\Python_logo_big.png"),
)

# widget
# label = ttk.Label(master=window, text="Spartan 3E", image=image_tk)
# label.pack()

# frame
button_frame = ttk.Frame(master=window)

button = ttk.Button(
    master=button_frame, text="        A button", image=python_logo_tk, compound="left"
)
button.pack(pady=10)

button_ctk = ctk.CTkButton(
    master=button_frame, text="        A button", image=img_ctk, compound="left"
)
button_ctk.pack(pady=10)

button_frame.grid(column=0, row=0, sticky="nsew")

# canvas for the image
canvas = tk.Canvas(master=window, background="black")
canvas.grid(column=1, columnspan=3, row=0, sticky="nsew")

# calling the function to alter image size on window changes
canvas.bind("<Configure>", keep_ratio)


# run
window.mainloop()
