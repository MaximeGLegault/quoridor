from typing import Tuple, Any

from game import Game


def print_tableau(tableau: [[Any]]) -> None:
    for x in reversed(tableau):
        print(x)


if __name__ == '__main__':
    game: Game = Game()
    print_tableau(game.tableau_des_pions)

