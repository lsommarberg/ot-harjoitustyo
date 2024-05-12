import unittest
from board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.example_puzzle = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"

    def test_board_exists(self):
        self.assertEqual(len(self.board.grid), 9)

    def test_initialize_grid_correct_for_value(self):
        board = Board()

        board.initialize_grid(self.example_puzzle)
        first_cell = board.get_cell(0, 0)
        self.assertEqual(first_cell.get_value(), 5)

    def test_initialize_grid_correct_for_0(self):
        board = Board()

        board.initialize_grid(self.example_puzzle)
        first_0 = board.get_cell(0, 2)
        self.assertEqual(first_0.get_value(), 0)

    def test_set_cell_value(self):
        board = Board()
        board.initialize_grid(self.example_puzzle)

        board.set_cell_value(0, 2, 1)

        result = board.get_cell(0, 2)
        self.assertEqual(result.get_value(), 1)

    def test_clear_cell(self):
        board = Board()
        board.initialize_grid(self.example_puzzle)
        board.set_cell_value(0, 2, 1)
        
        board.clear_cell(0, 2)

        result = board.get_cell(0, 2)

        self.assertEqual(result.get_value(), 0)


    def test_lock_cell(self):
        board = Board()
        board.lock_cell(0, 0)

        locked_cell = board.get_cell(0, 0)
        result = locked_cell.is_locked
        self.assertTrue(result)

    def test_clear_grid(self):
        board = Board()

        board.initialize_grid(self.example_puzzle)
        board.clear_grid()

        cleared_grid_first_value = board.grid[0][0].get_value()

        self.assertEqual(cleared_grid_first_value, 0)

