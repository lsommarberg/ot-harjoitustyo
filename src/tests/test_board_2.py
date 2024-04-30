import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.example_puzzle = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"

    def test_validate_col(self):
        board = Board()

        board.initialize_grid(self.example_puzzle)

        col = board.get_cells_in_col(0, 0)
        expected_output = [6, 0, 8, 4, 7, 0, 0, 0]
        self.assertEqual(col, expected_output)

    def test_validate_row(self):
        board = Board()

        board.initialize_grid(self.example_puzzle)

        col = board.get_cells_in_row(0, 0)
        expected_output = [3, 0, 0, 7, 0, 0, 0, 0]
        self.assertEqual(col, expected_output)

    def test_validate_box(self):
        board = Board()

        board.initialize_grid(self.example_puzzle)

        col = board.get_cells_in_box(0, 0)
        expected_output = [3, 0, 6, 0, 0, 0, 9, 8]
        self.assertEqual(col, expected_output)

    def test_not_valid_value(self):
        board = Board()

        board.initialize_grid(self.example_puzzle)

        res = board.validate(0, 2, 5)

        self.assertFalse(res)
