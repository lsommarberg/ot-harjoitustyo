import tkinter as tk


class SudokuBoard(tk.Frame):
    def __init__(self, parent, board):
        super().__init__(parent)
        self.board = board
        self.buttons = [[None for _ in range(9)] for _ in range(9)]

        self.create_buttons()

        self.notes_on = False

        self.bind_buttons()

    def create_buttons(self):
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
        for i in range(9):
            for j in range(9):
                self.buttons[i][j].bind("<Key>", self.buttons[i][j].key_pressed)

    def update_buttons(self):
        for i in range(9):
            for j in range(9):
                cell = self.board.get_cell(i, j)
                cell_value = cell.get_value()
                cell_notes = cell.get_notes()
                cell_is_locked = cell.is_locked
                cell_display_notes = cell.display_notes
                self.buttons[i][j].set_value(
                    str(cell_value),
                    locked=cell_is_locked,
                    notes=cell_notes,
                    display_notes=cell_display_notes,
                )

    def undo_button(self):
        self.board.undo_move()
        self.update_buttons()

    def notes_button(self):
        self.notes_on = not self.notes_on


class SudokuButton(tk.Button):
    def __init__(self, parent, row, col, board):
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

    def set_value(self, value=None, locked=None, notes=None, display_notes=None):
        if display_notes:
            note_matrix = [
                [str(n) if n != 0 else "" for n in notes[i * 3 : i * 3 + 3]]
                for i in range(3)
            ]
            note_text = "\n".join([" ".join(row) for row in note_matrix])
            self.config(text=note_text.strip(), fg="grey")
        else:
            if value != "0":
                self.config(text=value, fg="blue")
            else:
                self.config(text="", state="normal")
        if locked:
            self.config(text=value, fg="black")

    def cell_clicked(self):
        current_cell = self.board.get_cell(self.row, self.col)

        if not current_cell.is_locked:
            self.config(highlightbackground="red")
            self.focus_set()

    def key_pressed(self, event):
        if event.char.isdigit():
            value = int(event.char)
            if value:
                self.board.update_stack()
                if self.master.notes_on:
                    self.board.modify_notes(self.row, self.col, value)
                else:
                    self.board.make_move(self.row, self.col, value)

                self.master.update_buttons()

    def on_focus_in(self, _):
        self.config(highlightbackground="red")

    def on_focus_out(self, _):
        self.config(highlightbackground=self.default_bg)
