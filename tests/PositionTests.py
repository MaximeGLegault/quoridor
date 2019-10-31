import unittest

from Position import Position, PositionInvalide


class PositionTests(unittest.TestCase):
    def test_comme_jai_un_x_plus_petit_que_0_quand_je_creer_une_nouvelle_position_alors_raise_une_erreur(self):
        self.assertRaises(PositionInvalide, Position, -1, 0)


if __name__ == '__main__':
    unittest.main()
