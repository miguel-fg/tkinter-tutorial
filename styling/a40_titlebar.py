import customtkinter as ctk  # also works on normal tkinter

try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

"""
IMPORTANT NOTES:

Title bar color changes only work on Windows. This code will work on any OS thanks to the try-except clause
"""

# window
window = ctk.CTk(
    fg_color="#FF00FF"
)  # this will change the background of the app, not the title bar
window.title("This has a custom color")
window.geometry("300x200")

# change the title bar color
HWND = windll.user32.GetParent(window.winfo_id())  # actual window handle

try:
    title_bar_color = 0x000000FF  # For some reason, it's inverted (format: 0x00BBGGRR
    windll.dwmapi.DwmSetWindowAttribute(
        HWND,
        35,  # title bar identifier
        byref(
            c_int(title_bar_color)
        ),  # converts the color to the correct format Windows expects
        sizeof(c_int),  # if you remove this you explode
    )

    # title bar text color
    title_bar_text_color = (
        0x00FF0000  # For some reason, it's inverted (format: 0x00BBGGRR
    )
    windll.dwmapi.DwmSetWindowAttribute(
        HWND,
        36,  # title bar text identifier
        byref(
            c_int(title_bar_text_color)
        ),  # converts the color to the correct format Windows expects
        sizeof(c_int),  # if you remove this you explode
    )
except:
    pass
# run
window.mainloop()
