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

    def test_make_move_for_locked_cell(self):
        board = Board()
        board.initialize_grid(self.example_puzzle)
        set_value = board.make_move(0, 0, 1)

        result = board.get_cell(0, 0)
        self.assertEqual(result.get_value(), 5)
        self.assertFalse(set_value)

    def test_lock_cell(self):
        board = Board()
        board.lock_cell(0, 0)

        locked_cell = board.get_cell(0, 0)
        result = locked_cell.is_locked
        self.assertTrue(result)

    def test_update_stack(self):
        board = Board()

        board.initialize_grid(self.example_puzzle)
        board.update_stack()

        stack = board.undo_stack

        stack_instance = stack[0]
        stack_instance_first_cell = stack_instance[0][0].get_value()

        first_cell = board.get_cell(0, 0).value

        self.assertEqual(stack_instance_first_cell, first_cell)

    def test_undo_move(self):
        board = Board()
        board.initialize_grid(self.example_puzzle)
        board.update_stack()

        board.make_move(0, 2, 1)

        board.undo_move()

        self.assertEqual(board.get_cell(0, 2).value, 0)

    def test_modify_notes_no_notes(self):
        board = Board()
        board.initialize_grid(self.example_puzzle)

        board.modify_notes(0, 2, 1)

        modified_cell_notes = board.get_cell(0, 2).get_notes()

        expected_notes = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(modified_cell_notes, expected_notes)

    def test_modify_notes_remove_note(self):
        board = Board()
        board.initialize_grid(self.example_puzzle)

        board.modify_notes(0, 2, 1)
        board.modify_notes(0, 2, 1)

        modified_cell_notes = board.get_cell(0, 2).get_notes()

        expected_notes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(modified_cell_notes, expected_notes)
