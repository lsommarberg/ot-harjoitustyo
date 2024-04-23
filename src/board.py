import copy
from cell import Cell


class Board:
    def __init__(self):
        self.grid = [[Cell() for _ in range(9)] for _ in range(9)]
        self.undo_stack = []
        self.previous_state = None

    def initialize_grid(self, puzzle):
        for i in range(9):
            for j in range(9):
                value = puzzle[i * 9 + j]
                if value != "0":
                    self.grid[i][j].set_value(int(value))
                    self.grid[i][j].lock_cell()

    def get_cell(self, row, col):
        return self.grid[row][col]

    def set_cell_value(self, row, col, value):
        cell = self.get_cell(row, col)
        if not cell.is_locked:
            cell.set_value(value)
            return True
        return False

    def make_move(self, row, col, value):
        set_value = self.set_cell_value(row, col, value)
        if set_value:
            cell = self.get_cell(row, col)
            cell.display_notes = False
            return True
        return False

    def modify_notes(self, row, col, value):
        cell = self.get_cell(row, col)
        cell.display_notes = True
        cell.set_notes(value)
        return cell.notes

    def lock_cell(self, row, col):
        cell = self.get_cell(row, col)
        cell.lock_cell()

    def update_stack(self):
        grid_copy = [[Cell() for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                cell = self.get_cell(i, j)
                cell_value = cell.get_value()
                cell_notes = cell.get_notes()
                cell_is_locked = cell.is_locked
                cell_display_notes = cell.display_notes
                grid_copy[i][j].set_value(cell_value)
                grid_copy[i][j].notes = copy.deepcopy(cell_notes)
                grid_copy[i][j].is_locked = cell_is_locked
                grid_copy[i][j].display_notes = cell_display_notes

        self.undo_stack.append(grid_copy)

    def undo_move(self):
        if self.undo_stack:
            previous_state = self.undo_stack.pop()
            for i in range(9):
                for j in range(9):
                    cell_value = previous_state[i][j].get_value()
                    self.grid[i][j].set_value(cell_value)
                    cell_notes = previous_state[i][j].get_notes()

                    self.grid[i][j].notes = copy.deepcopy(cell_notes)
                    cell_display_notes = previous_state[i][j].display_notes
                    self.grid[i][j].display_notes = cell_display_notes
