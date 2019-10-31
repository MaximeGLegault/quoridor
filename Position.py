

class Position:

    def __init__(self, x, y):
        if self._out_of_bounds(x):
            raise PositionInvalide

        if self._out_of_bounds(y):
            raise PositionInvalide

        self.x = x
        self.y = y

    @staticmethod
    def _out_of_bounds(coordonnee: int):
        return coordonnee < 0 or coordonnee > 8

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x}, {self.y})"


class PositionInvalide(Exception):
    pass
