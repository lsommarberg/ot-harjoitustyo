import copy
from cell import Cell


class Board:
    """Object that handles the changes in sudoku board"""

    def __init__(self):
        self.grid = [[Cell() for _ in range(9)] for _ in range(9)]
        self.undo_stack = []
        self.max_undo_length = 20

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

    def make_move(self, row, col, value):
        """Make a player move to the given cell coordinates with a given value.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The value to be set
        """

        set_value = self.set_cell_value(row, col, value)
        if set_value:
            cell = self.get_cell(row, col)
            cell.display_notes = False
            valideted = self.validate(row, col, value)
            cell.value_is_valid = valideted

    def get_cells_in_box(self, row, col):
        """Make a list of other cells in the box of 9 based on a given cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            cells_in_box (list): other cells in the same box with the given cell
        """

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        cells_in_box = []

        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if i == row and j == col:
                    continue

                cells_in_box.append(self.grid[i][j].get_value())

        return cells_in_box

    def get_cells_in_col(self, row, col):
        """Make a list of other cells in the column based on a given cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            cells_in_col (list): other cells in the same column with the given cell
        """

        cells_in_col = []

        for i in range(9):
            if i == row:
                continue

            cells_in_col.append(self.grid[i][col].get_value())

        return cells_in_col

    def get_cells_in_row(self, row, col):
        """Make a list of other cells in the row based on a given cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            cells_in_row (list): other cells in the same row with the given cell
        """

        cells_in_row = [cell.get_value() for cell in self.grid[row]]

        cells_in_row.pop(col)

        return cells_in_row

    def validate(self, row, col, value):
        """Check if the user input value is already in the same box/cell/row

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The user input value

        Returns:
            False: if the cell is not valid (it is already int the same box/cell/row)
            True: if the cell is valid
        """

        if (
            int(value) in self.get_cells_in_box(row, col)
            or value in self.get_cells_in_col(row, col)
            or value in self.get_cells_in_row(row, col)
        ):
            return False
        return True

    def modify_notes(self, row, col, value):
        """Modify notes in the given cell

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The user input value

        """
        cell = self.get_cell(row, col)
        cell.display_notes = True
        cell.set_notes(value)

    def lock_cell(self, row, col):
        """Lock cell that will not be modified after setting up the original puzzle.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        """

        cell = self.get_cell(row, col)
        cell.lock_cell()

    def update_stack(self):
        """Update the undo stack to record the current state of the board for undo functionality."""

        grid_copy = self.get_board_state()

        self.undo_stack.append(grid_copy)

        if len(self.undo_stack) > self.max_undo_length:
            self.undo_stack.pop(0)

    def get_board_state(self):
        """Save the current state of the board."""

        grid_copy = [[copy.deepcopy(cell) for cell in row] for row in self.grid]
        return grid_copy

    def undo_move(self):
        """Set the board into the previous board state."""

        if self.undo_stack:
            previous_state = self.undo_stack.pop()
            previous_state_copy = [
                [copy.deepcopy(cell) for cell in row] for row in previous_state
            ]
            self.grid = copy.deepcopy(previous_state_copy)
