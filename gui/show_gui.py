from math import sqrt
from tkinter import *
from typing import List

from operations.color_conversions import invert_hex, Color


def show_gui(colors: List[Color]) -> None:
    window = Tk()
    window.title("Chromata")
    row = 0
    col = 0
    for color in colors:
        inv_col = invert_hex(color.hex_color)
        e = Label(window, text=color.hex_color, background=color.hex_color, font=(None, 16, "normal"), fg=inv_col)
        e.grid(row=row, column=col, sticky=E+W)
        row += 1
        if row > sqrt(len(colors)):
            row = 0
            col += 1
    window.mainloop()
