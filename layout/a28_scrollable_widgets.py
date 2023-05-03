import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self, size: tuple):
        super().__init__()

        # setup
        self.title("Scrolling widgets")
        self.geometry(f"{size[0]}x{size[1]}")

        # widgets
        self.text_list = [
            ("label", "button"),
            ("thing", "click"),
            ("third", "something"),
            ("label1", "button"),
            ("label2", "button"),
            ("label3", "button"),
            ("label4", "button"),
        ]
        self.list_frame = ListFrame(self, self.text_list, 100)

        # run
        self.mainloop()


class ListFrame(ttk.Frame):
    def __init__(self, parent: tk.Tk, text_data: list, item_height: int):
        super().__init__(master=parent)
        self.pack(expand=True, fill="both")

        # widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        # canvas
        # making a canvas larger than the frame
        self.canvas = tk.Canvas(
            master=self,
            background="red",
            scrollregion=(0, 0, self.winfo_width(), self.list_height),
        )
        self.canvas.pack(expand=True, fill="both")

        # display frame
        # frame that covers the entire canvas
        self.frame = ttk.Frame(master=self)

        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(
                expand=True, fill="both", pady=4, padx=10
            )

        # EXERCISE:
        # Make a scrollbar work

        self.scrollbar = ttk.Scrollbar(
            master=self, orient="vertical", command=self.canvas.yview
        )
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")

        # events
        self.canvas.bind_all(
            "<MouseWheel>", lambda e: self.canvas.yview_scroll(-e.delta // 60, "units")
        )
        self.bind(
            "<Configure>", self.update_size
        )  # updates the size to the correct one

    # draws a correctly sized canvas
    def update_size(self, event):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.canvas.bind_all(
                "<MouseWheel>",
                lambda e: self.canvas.yview_scroll(-e.delta // 60, "units"),
            )
            self.scrollbar.place(
                relx=1, rely=0, relheight=1, anchor="ne"
            )  # place the scrollbar again
        else:
            height = self.winfo_height()  # if the frame is smaller than the canvas
            self.canvas.unbind_all("<MouseWheel>")  # disable scrolling
            self.scrollbar.place_forget()  # remove the scrollbar

        self.canvas.create_window(
            (0, 0),
            window=self.frame,
            anchor="nw",
            width=self.winfo_width(),
            height=height,
        )

    # draws the list of items on the canvas
    def create_item(self, index, item):
        frame = ttk.Frame(master=self.frame)

        # grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0, 1, 2, 3, 4), weight=1, uniform="a")

        # widget
        ttk.Label(master=frame, text=f"#{index}").grid(row=0, column=0)
        ttk.Label(master=frame, text=item[0]).grid(row=0, column=1)
        ttk.Button(master=frame, text=item[1]).grid(
            row=0, column=2, columnspan=3, sticky="nsew"
        )

        return frame


App((500, 400))
