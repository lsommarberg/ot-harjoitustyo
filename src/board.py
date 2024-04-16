import copy
from cell import Cell


class Board:
    def __init__(self):
        self.grid = [[Cell() for _ in range(9)] for _ in range(9)]
        self.undo_stack = []

    def initialize_grid(self, puzzle):
        for i in range(9):
            for j in range(9):
                value = puzzle[i * 9 + j]
                if value != "0":
                    self.grid[i][j].set_value(int(value))
                    self.grid[i][j].lock_cell()
        self.update_stack()

    def get_cell(self, row, col):
        return self.grid[row][col]

    def set_cell_value(self, row, col, value):
        cell = self.get_cell(row, col)
        if not cell.is_locked:
            cell.set_value(value)
            return True
        return False

    def lock_cell(self, row, col):
        cell = self.get_cell(row, col)
        cell.lock_cell()

    def update_stack(self):
        self.undo_stack.append(copy.deepcopy(self.grid))

    def undo_move(self):
        if self.undo_stack:
            previous_state = self.undo_stack.pop()
            for row in range(9):
                for col in range(9):
                    cell_value = previous_state[row][col].get_value()
                    self.grid[row][col].set_value(cell_value)
