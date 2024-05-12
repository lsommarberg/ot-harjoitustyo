import unittest
from board import Board
from game_logic import GameLogic


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.example_puzzle = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
        self.example_puzzle_completed = "534678912672195348198342567859761423426853791713924856961537284287419635345286179"
        self.example_puzzle_not_completed = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"

    def test_validate_col(self):
        board = Board()

        game_logic = GameLogic(board)
        board.initialize_grid(self.example_puzzle)

        col = game_logic.get_cells_in_col(0, 0)
        expected_output = [6, 0, 8, 4, 7, 0, 0, 0]
        self.assertEqual(col, expected_output)

    def test_validate_row(self):
        board = Board()
        game_logic = GameLogic(board)

        board.initialize_grid(self.example_puzzle)

        col = game_logic.get_cells_in_row(0, 0)
        expected_output = [3, 0, 0, 7, 0, 0, 0, 0]
        self.assertEqual(col, expected_output)

    def test_validate_box(self):
        board = Board()
        game_logic = GameLogic(board)

        board.initialize_grid(self.example_puzzle)

        col = game_logic.get_cells_in_box(0, 0)
        expected_output = [3, 0, 6, 0, 0, 0, 9, 8]
        self.assertEqual(col, expected_output)

    def test_not_valid_value(self):
        board = Board()
        game_logic = GameLogic(board)

        board.initialize_grid(self.example_puzzle)

        res = game_logic.validate(0, 2, 5)

        self.assertFalse(res)

    def test_check_game_completion_true(self):
        test_board = Board()
        game_logic = GameLogic(test_board)

        test_board.initialize_grid(self.example_puzzle_completed)

        result = game_logic.check_game_completion()

        self.assertTrue(result)

    def test_check_game_completion_false(self):
        test_board = Board()

        game_logic = GameLogic(test_board)

        test_board.initialize_grid(self.example_puzzle_not_completed)

        result = game_logic.check_game_completion()

        self.assertFalse(result)

    def test_make_move_game_completed(self):
        test_board = Board()

        game_logic = GameLogic(test_board)
        example_puzzle_almost_completed = "530678912672195348198342567859761423426853791713924856961537284287419635345286179"

        test_board.initialize_grid(example_puzzle_almost_completed)

        game_logic.make_move(0, 2, 4)

        self.assertTrue(test_board.is_game_completed)
