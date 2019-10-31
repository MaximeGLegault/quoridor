from typing import Tuple, Any

from game import Game


if __name__ == '__main__':
    game: Game = Game()
    game.graphe.afficher_connections()
    print('\n')
    game.graphe.afficher_positions()

