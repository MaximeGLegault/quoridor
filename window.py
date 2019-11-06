from tkinter import *

from game_canvas import WindowBoard


class Window(Tk):

    def __init__(self):
        super().__init__()
        self.title("fuck")
        self.resizable(width=True, height=True)
        self.minsize(width=700, height=700)
        self.windowBoard = WindowBoard(self)
