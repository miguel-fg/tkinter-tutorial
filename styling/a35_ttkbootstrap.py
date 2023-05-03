import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

"""
    ttkbootstrap is an external module with better theme support.
    It applies themes to every widget
"""

class App(ttk.Window): #use ttk.Window() instead of tk.Tk()
    def __init__(self, size):
        super().__init__(themename="darkly")
        # setup
        self.title("ttk bootstrap intro")
        self.geometry(f"{size[0]}x{size[1]}")

        # widgets
        self.label = ttk.Label(master=self, text= "Label")
        self.label.pack(pady=10)

        self.button1 = ttk.Button(master=self, text="Red", bootstyle="danger")
        self.button1.pack(pady=10)                
        
        self.button2 = ttk.Button(master=self, text="Warning", bootstyle="warning")
        self.button2.pack(pady=10)                
        
        self.button3 = ttk.Button(master=self, text="Green", bootstyle="success")
        self.button3.pack(pady=10)                
        
        # run
        self.mainloop()

App((400,300))
