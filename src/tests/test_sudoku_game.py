import unittest
from sudoku_game import SudokuGameManager
from game_logic import GameLogic
from board import Board
from cell import Cell
from unittest.mock import MagicMock, patch


class TestGameManager(unittest.TestCase):
    def setUp(self):
        self.example_puzzle_completed = "534678912672195348198342567859761423426853791713924856961537284287419635345286179"
        self.example_puzzle_not_completed = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"

    def test_save_game_state(self):
        game_manager = SudokuGameManager(
            board=None, sudoku_board_ui=None, game_logic=None
        )

        game_manager.board = MagicMock()
        game_manager.db_handler = MagicMock()

        game_manager.board.is_game_completed = False

        game_manager.save_game_state()

        game_manager.db_handler.serialize_game_state.assert_called_once_with(
            game_manager.board.get_board_state()
        )
        game_manager.db_handler.insert_game_state.assert_called_once()

    def test_clear_game_state(self):
        game_manager = SudokuGameManager(
            board=None, sudoku_board_ui=None, game_logic=None
        )

        game_manager.board = MagicMock()
        game_manager.game_logic = MagicMock()

        game_manager.clear_game_state()

        game_manager.game_logic.clear_undo_stack.assert_called_once()

        game_manager.board.game_is_not_completed.assert_called_once()

    def test_fetch_puzzle(self):
        game_manager = SudokuGameManager(
            board=None, sudoku_board_ui=None, game_logic=None
        )

        game_manager.db_handler = MagicMock()
        game_manager.fetch_puzzle("Easy")

        game_manager.db_handler.get_puzzle_by_difficulty.assert_called_once_with("Easy")

    def test_start_new_game(self):
        game_manager = SudokuGameManager(
            board=None, sudoku_board_ui=None, game_logic=None
        )

        game_manager.board = MagicMock()
        game_manager.sudoku_board_ui = MagicMock()

        game_manager.db_handler = MagicMock()

        with patch.object(game_manager, "fetch_puzzle") as mock_fetch_puzzle:
            mock_fetch_puzzle.return_value = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
            game_manager.start_new_game("Easy")

            game_manager.board.clear_grid.assert_called_once()
            game_manager.board.initialize_grid.assert_called_once_with(
                "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
            )
            game_manager.sudoku_board_ui.update_buttons.assert_called_once()

    def test_continue_game(self):
        game_manager = SudokuGameManager(
            board=None, sudoku_board_ui=None, game_logic=None
        )

        game_manager.board = MagicMock()
        game_manager.sudoku_board_ui = MagicMock()

        game_manager.db_handler = MagicMock()

        with patch.object(
            game_manager.db_handler, "get_last_game_state"
        ) as mock_game_state:
            mock_game_state.return_value = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
            game_manager.continue_game()

            game_manager.board.clear_grid.assert_called_once()
            game_manager.sudoku_board_ui.update_buttons.assert_called_once()

    def test_restart_game(self):
        game_manager = SudokuGameManager(
            board=None, sudoku_board_ui=None, game_logic=None
        )

        game_manager.board = MagicMock()
        game_manager.sudoku_board_ui = MagicMock()

        game_manager.db_handler = MagicMock()
        game_manager.game_logic = MagicMock()

        with patch.object(
            game_manager, "initialize_grid_for_restart"
        ) as mock_game_state:
            mock_game_state.return_value = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
            game_manager.restart_game()

            game_manager.board.clear_grid.assert_called_once()
            game_manager.board.initialize_grid.assert_called_once_with(
                "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
            )
            game_manager.game_logic.clear_undo_stack.assert_called_once()
            game_manager.sudoku_board_ui.update_buttons.assert_called_once()

    def test_initialize_grid_for_restart(self):
        game_manager = SudokuGameManager(
            board=None, sudoku_board_ui=None, game_logic=None
        )

        game_manager.board = MagicMock()

        game_manager.db_handler = MagicMock()

        with patch.object(
            game_manager.db_handler, "get_last_game_state"
        ) as mock_game_state:
            mock_game_state.return_value = [
                [Cell() for _ in range(9)] for _ in range(9)
            ]
            result = game_manager.initialize_grid_for_restart()

            self.assertEqual(
                result,
                "000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            )
