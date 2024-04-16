import tkinter as tk
from board import Board
from UI.input_panel import ButtonPanel
from UI.sudoku_board import SudokuBoard


class SudokuApp:
    def __init__(self, root, puzzle):
        self.root = root
        self.root.title("Sudoku App")
        main_frame = tk.Frame(self.root)
        main_frame.grid(row=0, column=0, padx=10, pady=10)
        main_frame.config(bg="black")

        self.board = Board()
        self.sudoku_board = SudokuBoard(main_frame, self.board)
        self.sudoku_board.grid(row=0, column=0, padx=10, pady=10)
        self.sudoku_board.config(bg="black")

        self.button_panel = ButtonPanel(main_frame, self.sudoku_board)
        self.button_panel.grid(row=1, column=0, padx=10, pady=10)

        self.board.initialize_grid(puzzle)

        main_frame.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)

        self.sudoku_board.update_buttons()
