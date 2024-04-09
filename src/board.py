from cell import Cell


class Board:
    def __init__(self):
        self.grid = [[Cell() for _ in range(9)] for _ in range(9)]

    def initialize_grid(self, puzzle):
        for i in range(9):
            for j in range(9):
                value = puzzle[i * 9 + j]
                if value != "0":
                    self.grid[i][j].set_value(int(value))

    def set_groups(self):
        pass

    def get_cell(self, row, col):
        return self.grid[row][col]

    def set_cell_value(self, row, col, value):
        cell = self.get_cell(row, col)
        cell.set_value(value)
