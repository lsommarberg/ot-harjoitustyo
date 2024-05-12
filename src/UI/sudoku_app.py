import tkinter as tk
from board import Board
from sudoku_game import SudokuGameManager
from game_logic import GameLogic
from UI.input_panel import ButtonPanel
from UI.sudoku_board import SudokuBoardUI
from UI.game_start_dialog import GameStartDialog


class SudokuApp:
    """Represents the main Sudoku application.

    This class initializes and manages the Sudoku game application. It creates the main
    application window, sets up the game board, and
    handles user interactions for starting/continuing a game.

    Attributes:
        root: The Tkinter root window for the application.
        board: An instance of the Board class representing the Sudoku game board.
        main_frame: A Tkinter Frame widget serving as the main container for UI elements.
        sudoku_board_ui: An instance of the SudokuBoard class representing the graphical
                      representation of the Sudoku grid.
        button_panel: An instance of the ButtonPanel class representing the UI panel
                      containing game control buttons.
        sudoku_game_manager: An instance of the SudokuGameManager class that manages the changes
                            in the application and grid between the games.
        game_logic: An instance of the GameLogic class that manages the game logic.
    """

    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku App")
        self.main_frame = tk.Frame(self.root, bg="black")
        self.main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.board = Board()
        self.game_logic = GameLogic(self.board)
        self.sudoku_board_ui = SudokuBoardUI(
            self.main_frame, self.board, self.game_logic
        )
        self.sudoku_game_manager = SudokuGameManager(
            self.board, self.sudoku_board_ui, self.game_logic
        )

        self.sudoku_board_ui.bind("<<GameCompleted>>", self.handle_game_completed)

        self.game_option_dialog = GameStartDialog(self.root, self.sudoku_game_manager)

        self.sudoku_board_ui.grid(row=0, column=0, padx=10, pady=10)

        self.button_panel = ButtonPanel(self.main_frame, self.sudoku_board_ui)
        self.button_panel.grid(row=1, column=0, padx=10, pady=10)

        self.button_panel.bind("<<ReturnButton>>", self.handle_return)

        self.select_game_option()

    def select_game_option(self):
        self.root.wait_window(self.game_option_dialog.dialog)

    def handle_game_completed(self, _):
        self.game_option_dialog.dialog.destroy()
        self.sudoku_game_manager.clear_game_state()
        new_game_start_dialog = GameStartDialog(
            self.root,
            self.sudoku_game_manager,
            "Congratulations! You completed the game.",
        )

        self.root.wait_window(new_game_start_dialog.dialog)

    def handle_return(self, _):
        self.sudoku_game_manager.save_game_state()

        self.game_option_dialog.dialog.destroy()

        new_game_start_dialog = GameStartDialog(self.root, self.sudoku_game_manager)
        self.root.wait_window(new_game_start_dialog.dialog)

    def __del__(self):
        self.sudoku_game_manager.save_game_state()
        self.sudoku_game_manager.close()
