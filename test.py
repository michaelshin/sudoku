import unittest
import sudoku

class TestSudokuBoard(unittest.TestCase):
    def setUp(self):
        self.sudokuBoard = SudokuBoard()

class TestSudokuMove(unittest.TestCase):
    def test_valid_move(self):
        m = sudoku.SudokuMove("0 0 9")
        self.assertEquals(m.is_valid(), True)

    def test_invalid_move(self):
        m = sudoku.SudokuMove("0 0 -1")
        self.assertEquals(m.is_valid(), False)

if __name__ == "__main__":
    unittest.main()