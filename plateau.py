from Position import Position


class Plateau:
    def __init__(self):
        self.joueur_1: Position = Position(4, 0)
        self.joueur_2: Position = Position(4, 8)

    @staticmethod
    def creer_tableau_des_pions():
        tableau = []
        for x in range(9):
            tableau.append([])
            for y in range(9):
                tableau[x].append(' ')

        return tableau
