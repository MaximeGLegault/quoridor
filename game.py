from tkinter import Tk
from typing import Tuple, List

from graphe_du_jeu import GrapheDuJeu
from plateau import Plateau
from window import Window


class Game:

    def __init__(self):
        self.plateau = Plateau()
        self.graphe: GrapheDuJeu = GrapheDuJeu()

        self.window = Window()
        self.window.mainloop()

