import unittest
from board import Board
from game_logic import GameLogic


class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.example_puzzle = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"

    def test_make_move_for_locked_cell(self):
        board = Board()
        game_logic = GameLogic(board)
        board.initialize_grid(self.example_puzzle)

        set_value = game_logic.make_move(0, 0, 1)

        result = board.get_cell(0, 0)
        self.assertEqual(result.get_value(), 5)
        self.assertFalse(set_value)

    def test_update_stack(self):
        board = Board()
        game_logic = GameLogic(board)

        board.initialize_grid(self.example_puzzle)
        game_logic.update_stack()

        stack = game_logic.undo_stack

        stack_instance = stack[0]
        stack_instance_first_cell = stack_instance[0][0].get_value()

        first_cell = board.get_cell(0, 0).value

        self.assertEqual(stack_instance_first_cell, first_cell)

    def test_undo_move(self):
        board = Board()

        game_logic = GameLogic(board)

        board.initialize_grid(self.example_puzzle)
        game_logic.update_stack()

        game_logic.make_move(0, 2, 1)

        game_logic.undo_move()

        self.assertEqual(board.get_cell(0, 2).value, 0)

    def test_undo_move_stack_is_full(self):
        board = Board()
        game_logic = GameLogic(board)

        game_logic.max_undo_length = 3
        game_logic.update_stack()
        game_logic.make_move(0, 2, 1)

        game_logic.update_stack()
        game_logic.make_move(0, 2, 2)

        game_logic.update_stack()
        game_logic.make_move(0, 2, 3)

        game_logic.update_stack()
        game_logic.make_move(0, 2, 4)

        game_logic.undo_move()
        game_logic.undo_move()
        game_logic.undo_move()
        game_logic.undo_move()

        self.assertEqual(board.get_cell(0, 2).value, 1)

    def test_modify_notes_no_notes(self):
        board = Board()

        game_logic = GameLogic(board)
        board.initialize_grid(self.example_puzzle)

        game_logic.modify_notes(0, 2, 1)

        modified_cell_notes = board.get_cell(0, 2).get_notes()

        expected_notes = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(modified_cell_notes, expected_notes)

    def test_modify_notes_remove_note(self):
        board = Board()
        game_logic = GameLogic(board)

        board.initialize_grid(self.example_puzzle)

        game_logic.modify_notes(0, 2, 1)
        game_logic.modify_notes(0, 2, 1)

        modified_cell_notes = board.get_cell(0, 2).get_notes()

        expected_notes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(modified_cell_notes, expected_notes)
