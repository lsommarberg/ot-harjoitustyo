import copy
from cell import Cell


class Board:
    """Object that handles the changes made in sudoku board"""

    def __init__(self):
        self.grid = [[Cell() for _ in range(9)] for _ in range(9)]
        self.is_game_completed = False

    def initialize_grid(self, puzzle):
        """Sets the values of the puzzle for the cells of the Sudoku grid.

        Args:
            puzzle (str): a string representing the original puzzle"""

        for i in range(9):
            for j in range(9):
                value = puzzle[i * 9 + j]
                if value != "0":
                    self.grid[i][j].set_value(int(value))
                    self.grid[i][j].lock_cell()

    def clear_grid(self):
        """Clear the grid. """
        self.grid = [[Cell() for _ in range(9)] for _ in range(9)]

    def lock_cell(self, row, col):
        """Lock cell that will not be modified after setting up the original puzzle.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        """

        cell = self.get_cell(row, col)
        cell.lock_cell()

    def get_cell(self, row, col):
        """Retrieve the cell at the specified row and column coordinates.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            Cell: The cell object at the specified coordinates.
        """

        return self.grid[row][col]

    def set_cell_value(self, row, col, value):
        """Set a value to a cell at the specified row and column coordinates.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The value to be set

        Returns:
            True if setting the value succeeded.
            False if the cell was locked
        """

        cell = self.get_cell(row, col)
        if not cell.is_locked:
            cell.set_value(value)
            return True
        return False

    def clear_cell(self, row, col):
        """Clear cell at the specified row and column coordinates.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        
        """

        cell = self.get_cell(row, col)
        cell.set_value(0)

    def set_cell_notes(self, row, col, value):
        """Set notes to the cell at the specified row and column coordinates.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The value to be set
        
        """
        cell = self.get_cell(row, col)
        cell.display_notes = True
        cell.set_notes(value)

    def restore_state(self, state):
        """Restore the board to a previous state."""
        self.grid = [[copy.deepcopy(cell) for cell in row] for row in state]

    def get_board_state(self):
        """Save the current state of the board."""

        grid_copy = [[copy.deepcopy(cell) for cell in row] for row in self.grid]
        return grid_copy

    def game_is_completed(self):
        """Set the game as completed."""

        self.is_game_completed = True

    def game_is_not_completed(self):
        """Set the game as not completed."""

        self.is_game_completed = False
