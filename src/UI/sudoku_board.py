import tkinter as tk


class SudokuBoardUI(tk.Frame):
    """A graphical representation of a Sudoku board within the main frame window."""

    def __init__(self, parent, board, game_logic):
        """Constructor

        Attributes:
            notes_on: A boolean indicating whether the notes mode is enabled.
            buttons: A 2D list of Button objects representing the cells of the Sudoku grid.

        Args:
            parent: The main frame window
            board: Board object representing the Sudoku puzzle.

        """
        super().__init__(parent, bg="black")
        self.board = board
        self.buttons = [[None for _ in range(9)] for _ in range(9)]

        self.game_logic = game_logic

        self.create_buttons()

        self.notes_on = False

        self.bind_buttons()

    def create_buttons(self):
        """Create the buttons representing the cells of the Sudoku grid."""

        button_size = 3
        for i in range(9):
            for j in range(9):
                padx, pady = 0, 0
                if i % 3 == 0 and i != 0:
                    pady = 3
                if j % 3 == 0 and j != 0:
                    padx = 3

                button = SudokuButton(self, i, j, self.board)
                button.grid(row=i, column=j, padx=(padx, 0), pady=(pady, 0))
                button.config(width=button_size, height=button_size, bg="white")
                self.buttons[i][j] = button

    def bind_buttons(self):
        """Bind events to the buttons."""

        for i in range(9):
            for j in range(9):
                self.buttons[i][j].bind("<Key>", self.buttons[i][j].key_pressed)

    def update_buttons(self):
        """Update the display of the Sudoku grid based on the current state of the Board object."""

        for i in range(9):
            for j in range(9):
                cell = self.board.get_cell(i, j)
                cell_value = cell.get_value()
                cell_notes = cell.get_notes()
                cell_is_locked = cell.is_locked
                cell_display_notes = cell.display_notes
                cell_value_is_valid = cell.value_is_valid

                self.buttons[i][j].set_value(
                    str(cell_value),
                    locked=cell_is_locked,
                    notes=cell_notes,
                    display_notes=cell_display_notes,
                    value_is_valid=cell_value_is_valid,
                )

    def undo_button(self):
        """Handle the event when the "Undo" button is clicked."""

        self.game_logic.undo_move()
        self.update_buttons()

    def notes_button(self):
        """Handle the event when the "Notes" button is clicked."""

        self.notes_on = not self.notes_on

    def completed_game(self):
        self.event_generate("<<GameCompleted>>", when="tail")


class SudokuButton(tk.Button):
    """A graphical representation of the cells (buttons) of the sudoku grid."""

    def __init__(self, parent, row, col, board):
        """Constructor for a Sudoku board button.

        Args:
            parent (tk.Widget): The parent (main frame) widget to which the button belongs.
            row (int): The row index of the button.
            col (int): The column index of the button.
            board (Board): The Sudoku board object to which the button belongs.
        """
        super().__init__(
            parent,
            width=2,
            height=2,
            padx=2,
            pady=2,
            bd=1,
            relief="solid",
            command=self.cell_clicked,
        )
        self.row = row
        self.col = col
        self.board = board
        self.default_bg = self.cget("bg")

        self.bind("<Key>", self.key_pressed)
        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

    def set_value(
        self,
        value=None,
        locked=None,
        notes=None,
        display_notes=None,
        value_is_valid=None,
    ):
        """Set values to the grid when buttons are updated."""

        if display_notes:
            note_matrix = [
                [str(n) if n != 0 else "" for n in notes[i * 3 : i * 3 + 3]]
                for i in range(3)
            ]
            note_text = "\n".join([" ".join(row) for row in note_matrix])
            self.config(text=note_text.strip(), fg="grey")
        else:
            if value != "0":
                if value_is_valid:
                    color = "blue"
                else:
                    color = "red"
                self.config(text=value, fg=color)
            else:
                self.config(text="", state="normal")
        if locked:
            self.config(text=value, fg="black")

    def cell_clicked(self):
        """Handle the event when the cell (button) is clicked."""

        current_cell = self.board.get_cell(self.row, self.col)

        if not current_cell.is_locked:
            self.config(highlightbackground="green")
            self.focus_set()

    def key_pressed(self, event):
        """Handle the event when the user sets values to the grid."""

        if event.char.isdigit():
            value = int(event.char)
            if value == 0:
                self.master.game_logic.update_stack()
                self.board.clear_cell(self.row, self.col)
                self.master.update_buttons()
            else:
                self.master.game_logic.update_stack()
                if self.master.notes_on:
                    self.master.game_logic.modify_notes(self.row, self.col, value)
                else:
                    self.master.game_logic.make_move(self.row, self.col, value)

                self.master.update_buttons()
                if self.board.is_game_completed:
                    self.master.completed_game()

    def on_focus_in(self, _):
        """Callback function called when the button gains focus."""

        self.config(highlightbackground="green")

    def on_focus_out(self, _):
        """Callback function called when the button loses focus."""

        self.config(highlightbackground=self.default_bg)
