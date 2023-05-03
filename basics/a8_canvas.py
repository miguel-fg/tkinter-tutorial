import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry("600x600")
window.title("Canvas")

# canvas
canvas = tk.Canvas(master=window, bg="white")
canvas.pack()

# rectangle
canvas.create_rectangle(
    (50, 20, 100, 200),  # (distance from) left, top, right, bottom
    fill="red",
    width=10,
    dash=(1, 2),  # (dash length, gap length)
    outline="green",
)

# line
canvas.create_line((0, 0, 100, 150), fill="blue")

# oval
canvas.create_oval((200, 0, 300, 100), fill="pink")

# polygon
canvas.create_polygon((0, 0, 100, 200, 300, 50, 150, -50), fill="gray")

# arc
canvas.create_arc(
    (200, 0, 300, 100),
    fill="red",
    start=45,  # start offset angle
    extent=180,  # length of the arc
    style=tk.ARC,  # default is PIESLICE
    outline="yellow",
    width=10,
)

canvas2 = tk.Canvas(master=window, bg="gray")
canvas2.pack()

# text
canvas2.create_text((100, 100), text="this is some text")

# widgets
canvas2.create_window(
    (150, 150), window=ttk.Button(master=window, text="this is a label in a canvas")
)

# EXERCISE
# use event binding to create a basic paint app
brush_size = 4


def paint_func(event):
    x = event.x
    y = event.y
    r = brush_size / 2
    canvas2.create_oval(
        (
            x + r,
            y + r,
            x - r,
            y - r,
        ),
        fill="pink",
        width=0,
    )


def brush_size_adjust(event):
    global brush_size

    if event.delta > 0:
        brush_size += 4
    else:
        brush_size -= 4

    brush_size = max(0, min(brush_size, 50))


canvas2.bind("<Motion>", paint_func)
canvas2.bind("<MouseWheel>", brush_size_adjust)

# run
window.mainloop()
