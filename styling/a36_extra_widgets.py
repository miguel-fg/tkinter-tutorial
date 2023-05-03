import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter

class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")

        # setup
        self.title("extra widgets")

        # scrollframe
        self.scroll_frame = ScrolledFrame(master=self)
        self.scroll_frame.pack(expand=True, fill="both")

        for i in range(100):
            ttk.Label(master=self.scroll_frame, text=f"Label: {i}").pack(fill="x")
            ttk.Button(master=self.scroll_frame, text=f"Button: {i}").pack(fill="x")

        # toast
        # small notification
        self.toast = ToastNotification(
            title="This is a message title",
            message = "This is the actual message",
            duration=2000,
            bootstyle="dark",
            position=(50,100, "ne")) # padx, pady, position 
        
        # is you use self.toast.show_toast() by itself, the main window will disappear with it
        # show toast button
        ttk.Button(master=self, text="show toast", command= self.toast.show_toast).pack(pady=10)

        # tooltip
        self.button = ttk.Button(master=self, text="tooltip button", bootstyle="warning")
        self.button.pack(pady=10)               

        ToolTip(widget=self.button, text="This does something", bootstyle="danger-inverse")

        # calendar
        self.calendar = DateEntry(master=self)
        self.calendar.pack(pady=10)

        ttk.Button(master=self, text="get calendar date", command= lambda: print(self.calendar.entry.get())).pack()        

        #progress bar -> floodgauge
        self.progress_int = tk.IntVar(value=50)
        self.progress = ttk.Floodgauge(
            master=self,
            text="progress", 
            variable = self.progress_int,
            bootstyle = "danger",
            mask = "{}%" #automatically displays the value of the progress bar
        )
        
        self.progress.pack(pady=10, fill="x")
        ttk.Scale(master=self, from_ = 0, to=100, variable=self.progress_int).pack()        

        # meter
        ttk.Meter(
            master=self, 
            bootstyle="success", 
            subtextstyle="warning", 
            subtext="This is a meter",
            padding=5,
            amountused=30,
            interactive=True
        ).pack()            
        
        # run
        self.mainloop()

App()