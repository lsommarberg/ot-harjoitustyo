import tkinter as tk


class SudokuBoard(tk.Frame):
    def __init__(self, parent, board, entry_widget):
        super().__init__(parent)
        self.board = board
        self.entry_widget = entry_widget
        self.buttons = [[None for _ in range(9)] for _ in range(9)]

        self.create_buttons()

    def create_buttons(self):
        for i in range(9):
            for j in range(9):
                button = SudokuButton(self, i, j, self.board, self.entry_widget)
                button.grid(row=i, column=j, padx=1, pady=1)
                self.buttons[i][j] = button

    def update_buttons(self):
        for i in range(9):
            for j in range(9):
                cell_value = self.board.get_cell(i, j).get_value()
                self.buttons[i][j].set_value(str(cell_value))


class SudokuButton(tk.Button):
    def __init__(self, parent, row, col, board, entry_widget):
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
        self.entry_widget = entry_widget

    def set_value(self, value):
        if value != "0":
            self.config(text=value, state="disabled", disabledforeground="black")
        else:
            self.config(text="", state="normal")

    def cell_clicked(self):
        value = self.entry_widget.get()
        if value:
            self.board.set_cell_value(self.row, self.col, int(value))

            cell_value = self.board.get_cell(self.row, self.col).get_value()
            if cell_value != 0:
                self.config(text=str(cell_value))
            else:
                self.config(text="")
