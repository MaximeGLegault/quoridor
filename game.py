from typing import Tuple, List

from plateau import Plateau


class Game:

    def __init__(self):
        self.tableau_des_connections: List[List[Tuple[int, int]]] = Plateau.creer_tableau_avec_connections_en_croix()
        self.tableau_des_pions: List[List[str]] = Plateau.creer_tableau_des_pions()

