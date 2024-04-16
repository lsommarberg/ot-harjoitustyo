from board import Board
from UI.input_panel import ButtonPanel
from UI.sudoku_board import SudokuBoard


class SudokuApp:
    def __init__(self, root, puzzle):
        self.root = root
        self.root.title("Sudoku App")

        self.board = Board()
        self.sudoku_board = SudokuBoard(self.root, self.board)
        self.button_panel = ButtonPanel(self.root, self.sudoku_board)

        self.board.initialize_grid(puzzle)

        self.button_panel.grid(row=2, column=0)

        self.sudoku_board.grid(row=0, column=0)

        self.sudoku_board.update_buttons()

        self.board.initialize_grid(puzzle)
