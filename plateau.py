from typing import List, Tuple


class Plateau:
    def __init__(self):
        self.plateau_de_connection: List[List[Tuple[int, int]]] = Plateau.creer_tableau_avec_connections_en_croix()
        self.murs_horizontals: List[Tuple[int, int]] = []
        self.murs_verticals: List[Tuple[int, int]] = []

    def bouger_pion(self, pion: str, emplacement: (int, int)) -> None:
        pass

    @staticmethod
    def creer_tableau_avec_connections_en_croix() -> List[List[Tuple[int, int]]]:
        tableau = []
        for x in range(9):
            tableau.append([])
            for y in range(9):
                tableau[x].append([])
                if x - 1 >= 0:
                    tableau[x][y].append((x - 1, y))
                if x + 1 <= 8:
                    tableau[x][y].append((x + 1, y))
                if y - 1 >= 0:
                    tableau[x][y].append((x, y - 1))
                if y + 1 <= 8:
                    tableau[x][y].append((x, y + 1))
        return tableau

    @staticmethod
    def creer_tableau_des_pions():
        tableau = []
        for x in range(9):
            tableau.append([])
            for y in range(9):
                tableau[x].append(' ')

        return tableau
