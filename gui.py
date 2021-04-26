from math import sqrt
from tkinter import *

from color_conversions import invert_hex


def gui(colors) -> None:
    window = Tk()
    window.title("Chromata")
    row = 0
    col = 0
    for color in colors:
        inv_col = invert_hex(color)
        e = Label(window, text=color, background=color, font=(None, 16, "normal"), fg=inv_col)
        e.grid(row=row, column=col, sticky=E+W)
        row += 1
        if row > sqrt(len(colors)):
            row = 0
            col += 1
    window.mainloop()
