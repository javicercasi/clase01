import unittest

from sudo import Sudoku


class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.game= Sudoku(["53xx7xxxx",
                           "6xx195xxx",
                           "x98xxxx6x",
                           "8xxx6xxx3",
                           "4xx8x3xx1",
                           "7xxx2xxx6",
                           "x6xxxx28x",
                           "x3x419xx5",
                           "xxxx8xx79"])
        

        self.assertTrue(self.game.is_playing) 
    def test_error(self):

        self.assertFalse(self.game.valores_fijos(0,0))
        self.assertFalse(self.game.repeticion_fila_columna(0,2,'7'))
        self.assertFalse(self.game.repeticion_zona(8,6,'2'))
        self.assertFalse(self.game.general(8,6,'8'))
        self.assertFalse(self.game.general(0,0,'8'))

    def test_error(self):
        

    def test_valor_disponible(self):

        self.assertTrue(self.game.valores_fijos(1,1))
        self.assertTrue(self.game.repeticion_fila_columna(0,8,'4'))
        self.assertTrue(self.game.repeticion_zona(8,1,'1'))
        self.assertTrue(self.game.repeticion_zona(3,7,'7'))
        


if __name__ == '__main__':
    unittest.main()
