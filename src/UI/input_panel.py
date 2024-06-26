import tkinter as tk


class ButtonPanel(tk.Frame):
    def __init__(self, parent, sudoku_board):
        super().__init__(parent)
        self.sudoku_board = sudoku_board

        self.notes_button = tk.Button(
            self, text="Notes", width=15, height=1, command=self.notes_clicked
        )
        self.notes_button.grid(row=0, column=0, padx=5)
        self.default_button_color = self.notes_button.cget("bg")

        self.undo_button = tk.Button(
            self, text="Undo", width=15, height=1, command=self.undo_button_clicked
        )
        self.undo_button.grid(row=0, column=1, padx=5)

        self.return_button = tk.Button(
            self, text="Return", width=15, height=1, command=self.return_button_clicked
        )
        self.return_button.grid(row=0, column=2, padx=5)

    def undo_button_clicked(self):
        self.sudoku_board.undo_button()

    def notes_clicked(self):
        self.sudoku_board.notes_button()
        self.set_notes_button_color(self.sudoku_board.notes_on)

    def set_notes_button_color(self, notes_on):
        if notes_on:
            self.notes_button.configure(bg="green")
        else:
            self.notes_button.config(bg=self.default_button_color)

    def return_button_clicked(self):
        self.event_generate("<<ReturnButton>>", when="tail")
