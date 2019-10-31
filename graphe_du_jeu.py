from typing import List, Dict

from Position import Position

Connections = List[Position]
Graphe = Dict[Position, List[Position]]


class GrapheDuJeu:

    def __init__(self):
        self.dictionnaire_des_connections: Graphe = GrapheDuJeu.creer_graphe_complet_sans_pions()
        self.liste_des_positions = GrapheDuJeu.creer_liste_des_positinos()
        self._modifier_les_connections_pour_les_positions_de_depart_du_joueur(Position(0, 4))
        self._modifier_les_connections_pour_les_positions_de_depart_du_joueur(Position(8, 4))

    @staticmethod
    def creer_liste_des_positinos():
        tableau = []
        for x in range(9):
            tableau.append([])
            for y in range(9):
                tableau[x].append(Position(x, y))
        return tableau

    @staticmethod
    def creer_graphe_complet_sans_pions() -> Graphe:
        dictionnaire_des_connections = {}
        for y in range(9):
            for x in range(9):
                dictionnaire_des_connections[Position(x, y)] = []
                if x - 1 >= 0:
                    dictionnaire_des_connections[Position(x, y)].append(Position(x - 1, y))
                if x + 1 <= 8:
                    dictionnaire_des_connections[Position(x, y)].append(Position(x + 1, y))
                if y - 1 >= 0:
                    dictionnaire_des_connections[Position(x, y)].append(Position(x, y - 1))
                if y + 1 <= 8:
                    dictionnaire_des_connections[Position(x, y)].append(Position(x, y + 1))

        return dictionnaire_des_connections

    def _modifier_les_connections_pour_les_positions_de_depart_du_joueur(self, position: Position) -> None:
        self._modifier_les_connections_a_gauche_et_droite_de_la_postion_de_depart(position)
        self._modifier_les_connections_en_bas_ou_haut_de_la_postion_de_depart(position)

    def _modifier_les_connections_en_bas_ou_haut_de_la_postion_de_depart(self, position: Position) -> None:
        x, y = position.x, position.y
        if position.x == 8:
            position_dou_il_faut_supprimer_la_connection = Position(x - 1, y)
        else:
            position_dou_il_faut_supprimer_la_connection = Position(x + 1, y)

        self.dictionnaire_des_connections[position_dou_il_faut_supprimer_la_connection].remove(position)
    
    def _modifier_les_connections_a_gauche_et_droite_de_la_postion_de_depart(self, position: Position) -> None:
        position_a_gauche_de_la_position = Position(position.x, position.y - 1)
        position_a_droite_de_la_position = Position(position.x, position.y + 1)

        connections_a_gauche_du_joueur = self.dictionnaire_des_connections[position_a_gauche_de_la_position]
        connections_a_droite_du_joueur = self.dictionnaire_des_connections[position_a_droite_de_la_position]

        connections_a_droite_du_joueur.remove(position)
        connections_a_droite_du_joueur.append(position_a_gauche_de_la_position)

        connections_a_gauche_du_joueur.remove(position)
        connections_a_gauche_du_joueur.append(position_a_droite_de_la_position)

    def convertir_en_liste(self) -> List[List[List[Position]]]:
        liste = []
        for x in range(9):
            liste.append([])
            for y in range(9):
                liste[x].append(self.dictionnaire_des_connections.get(Position(x, y)))

        return liste

    def afficher_connections(self):
        for x in (self.convertir_en_liste()):
            string_buffer = ""

            def function(y):
                missing_length = 4 - len(y)
                for i in range(missing_length):
                    y.append('    ')
                return y

            new_x = map(function, x)
            for y in new_x:
                string_buffer += str(y)
                string_buffer += ' -|- '
            print(string_buffer)

    def afficher_positions(self):
        for x in self.liste_des_positions:
            print(x)
