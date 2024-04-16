import tkinter as tk


class SudokuBoard(tk.Frame):
    def __init__(self, parent, board):
        super().__init__(parent)
        self.board = board
        self.buttons = [[None for _ in range(9)] for _ in range(9)]
        self.undo_stack = []

        self.create_buttons()

        self.bind_buttons()

    def create_buttons(self):
        for i in range(9):
            for j in range(9):
                padx, pady = 0, 0
                if i % 3 == 0 and i != 0:
                    pady = 5
                if j % 3 == 0 and j != 0:
                    padx = 5

                button = SudokuButton(self, i, j, self.board)
                button.grid(row=i, column=j, padx=(padx, 0), pady=(pady, 0))
                self.buttons[i][j] = button

    def bind_buttons(self):
        for i in range(9):
            for j in range(9):
                self.buttons[i][j].bind("<Key>", self.buttons[i][j].key_pressed)

    def update_buttons(self):
        for i in range(9):
            for j in range(9):
                cell_value = self.board.get_cell(i, j).get_value()
                self.buttons[i][j].set_value(str(cell_value))

    def undo_button(self):
        self.board.undo_move()
        self.update_buttons()


class SudokuButton(tk.Button):
    def __init__(self, parent, row, col, board):
        super().__init__(
            parent,
            width=2,
            height=2,
            padx=2,
            pady=2,
            bd=0,
            relief="solid",
            command=self.cell_clicked,
        )
        self.row = row
        self.col = col
        self.board = board
        self.default_bg = self.cget("bg")

        self.bind("<Key>", self.key_pressed)

    def set_value(self, value, color=None):
        if value != "0":
            self.config(text=value, fg=color)
        else:
            self.config(text="", state="normal")
        self.config(borderwidth=0, highlightbackground=self.default_bg)

    def cell_clicked(self):
        current_cell = self.board.get_cell(self.row, self.col)

        if not current_cell.is_locked:
            self.config(highlightbackground="red")
            self.focus_set()

    def key_pressed(self, event):
        if event.char.isdigit():
            value = int(event.char)
            new_value = self.board.set_cell_value(self.row, self.col, value)
            if new_value:
                self.board.update_stack()
                self.set_value(str(value), color="blue")
