import unittest

from sudo import Sudoku


class TestSudoku(unittest.TestCase):
    def Setup(self):
        game= Sudoku()
        game.string_converter = (["53xx7xxxx",
                         "6xx195xxx",
                         "x98xxxx6x",
                         "8xxx6xxx3",
                         "4xx8x3xx1",
                         "7xxx2xxx6",
                         "x6xxxx28x",
                         "x3x419xx5",
                         "xxxx8xx79"])

        self.assertFalse(Sudoku.is_playing) 
        print (matriz)
                
    
    """def test_play_incorrecto(self):
        result = self.game.panel_numero(1, 1, 3)
        self.assertFalse(self.game.poner_numero(1, 1, 3), 'El lugar esta ocupado')
        self.assertTrue(self.game.is_playing)

    def test_play_correcto(self):
        result = self.game.panel_numero(3, 1, 3)
        self.assertFalse(self.game.poner_numero(3, 1, 3), result)
        self.assertTrue(self.game.is_playing)
    """
if __name__ == '__main__':
    unittest.main()
