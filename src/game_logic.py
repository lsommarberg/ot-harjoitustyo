class GameLogic:
    def __init__(self, board):
        """Handle the game logic for Sudoku."""

        self.board = board
        self.undo_stack = []
        self.max_undo_length = 20

    def make_move(self, row, col, value):
        """Make a player move to the given cell coordinates with a given value.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
            value (int): The value to be set
        """

        set_value = self.board.set_cell_value(row, col, value)
        if set_value:
            cell = self.board.get_cell(row, col)
            cell.display_notes = False
            valideted = self.validate(row, col, value)
            cell.value_is_valid = valideted
            if valideted:
                is_completed = self.check_game_completion()
                if is_completed:
                    self.board.game_is_completed()

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

                cells_in_box.append(self.board.grid[i][j].get_value())

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

            cells_in_col.append(self.board.grid[i][col].get_value())

        return cells_in_col

    def get_cells_in_row(self, row, col):
        """Make a list of other cells in the row based on a given cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            cells_in_row (list): other cells in the same row with the given cell
        """

        cells_in_row = [cell.get_value() for cell in self.board.grid[row]]

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
        self.board.set_cell_notes(row, col, value)

    def update_stack(self):
        """Update the undo stack to record the current state of the board for undo functionality."""

        grid_copy = self.board.get_board_state()

        self.undo_stack.append(grid_copy)

        if len(self.undo_stack) > self.max_undo_length:
            self.undo_stack.pop(0)

    def undo_move(self):
        """Set the board into the previous board state."""
        if self.undo_stack:
            previous_state = self.undo_stack.pop()
            self.board.restore_state(previous_state)

    def check_game_completion(self):
        """Check if the game is completed or not.
        
            Returns:
            False: if the game is not completed
            True: if the game is completed
        """

        for row in range(9):
            for col in range(9):
                cell_value = self.board.get_cell(row, col).get_value()

                if cell_value == 0 or not self.validate(row, col, cell_value):
                    return False

        return True

    def clear_undo_stack(self):
        self.undo_stack = []
