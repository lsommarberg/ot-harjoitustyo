class Cell:
    """Object representing individual cells on the Sudoku board."""

    def __init__(self, value=0):
        """Initialize a cell object.

        Args:
            value (int, optional): The initial value of the cell. Default is 0.

        Attributes:
            value (int): The current value of the cell.
            is_locked (bool): A flag indicating whether the cell is locked.
            notes (list): A list representing notes for the cell.
            display_notes (bool): A flag indicating whether to display notes for the cell.
            value_is_valid (bool): A flag indicating whether the current value of the cell is valid.
        """
        self.value = value
        self.is_locked = False
        self.notes = [0] * 9
        self.display_notes = False
        self.value_is_valid = True

    def set_value(self, value):
        """Set value to the cell.
        Args:
            value (int): the value to be set
        """

        self.value = value

    def lock_cell(self):
        """Lock cell by setting the is_locked flag to True"""

        self.is_locked = True

    def get_value(self):
        """Return the value of the cell"""

        return self.value

    def get_notes(self):
        """Return the notes of the cell"""

        return self.notes

    def set_notes(self, value):
        """Modifiy notes of the cell.
        Args:
            value (int): value to be added/removed

        """

        if self.notes[value - 1] == 0:
            self.notes[value - 1] = value
        else:
            self.notes[value - 1] = 0
