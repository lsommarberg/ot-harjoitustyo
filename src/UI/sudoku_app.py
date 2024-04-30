import tkinter as tk
from board import Board
from UI.input_panel import ButtonPanel
from UI.sudoku_board import SudokuBoard
from database import DatabaseHandler


class GameStartDialog:
    """Object that handles the starting dialog for the Sudoku game.

    This dialog allows the player to select the difficulty level for a new game.

    Attributes:
        parent: The parent widget for the dialog.
        result: A tuple containing the result of the dialog. The first element
                indicates the action chosen (e.g., "New Game"), and the second
                element indicates the selected difficulty level.
        dialog: The Toplevel widget representing the dialog window.
        label: A Label widget displaying the instruction to choose the difficulty.
        difficulty_var: A StringVar representing the selected difficulty level.
        difficulty_options: A list of difficulty options available in the dropdown menu.
        dropdown: An OptionMenu widget for selecting the difficulty level.
        new_game_button: A Button widget for starting a new game.
    """

    def __init__(self, parent):
        self.parent = parent
        self.result = None

        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Select Difficulty")

        self.dialog.transient(parent)

        self.label = tk.Label(self.dialog, text="Choose Difficulty:")
        self.label.pack()

        self.difficulty_var = tk.StringVar(self.dialog)
        self.difficulty_var.set("Easy")
        self.difficulty_options = ["Easy", "Medium", "Hard"]
        self.dropdown = tk.OptionMenu(
            self.dialog, self.difficulty_var, *self.difficulty_options
        )
        self.dropdown.pack()

        self.new_game_button = tk.Button(
            self.dialog, text="New Game", command=self.new_game
        )
        self.new_game_button.pack()
        self.dialog.geometry("450x300")

    def new_game(self):
        selected_difficulty = self.difficulty_var.get()
        self.result = ("New Game", selected_difficulty)
        self.dialog.destroy()


class SudokuApp:
    """Represents the main Sudoku application.

    This class initializes and manages the Sudoku game application. It creates the main
    application window, sets up the game board, loads puzzles from the database, and
    handles user interactions for starting a new game.

    Attributes:
        root: The Tkinter root window for the application.
        board: An instance of the Board class representing the Sudoku game board.
        main_frame: A Tkinter Frame widget serving as the main container for UI elements.
        sudoku_board: An instance of the SudokuBoard class representing the graphical
                      representation of the Sudoku grid.
        button_panel: An instance of the ButtonPanel class representing the UI panel
                      containing game control buttons.
        db_handler: An instance of the DatabaseHandler class for interacting with the
                    SQLite database storing Sudoku puzzles.
    """

    def __init__(self, root):
        """Initializes the Sudoku application.

        Args:
            root: The Tkinter root window for the application.
        """
        db_file = "sudoku.db"
        self.db_handler = DatabaseHandler(db_file)
        self.initialize_with_default_puzzles()

        self.root = root
        self.root.title("Sudoku App")

        self.board = Board()
        self.main_frame = tk.Frame(self.root, bg="black")
        self.main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.sudoku_board = SudokuBoard(self.main_frame, self.board)
        self.sudoku_board.grid(row=0, column=0, padx=10, pady=10)

        self.button_panel = ButtonPanel(self.main_frame, self.sudoku_board)
        self.button_panel.grid(row=1, column=0, padx=10, pady=10)

        self.select_game_option()

    def initialize_with_default_puzzles(self):
        """Initializes the database with default Sudoku puzzles.

        Inserts a set of predefined Sudoku puzzles into the database with varying
        difficulty levels.

        """
        puzzles = [
            (
                "530070000600195000098000060800060003400803001700020006060000280000419005000080079",
                "Easy",
            ),
            (
                "002008040000000000109000000000050207000000000305602000000000076000000000080104300",
                "Medium",
            ),
            (
                "000000000090060000085000003600000040001300000050700000040000800000010002007000450",
                "Hard",
            ),
        ]
        for puzzle, difficulty in puzzles:
            self.db_handler.insert_puzzle(puzzle, difficulty)

    def select_game_option(self):
        """Displays the game start dialog and handles user selection."""
        game_option_dialog = GameStartDialog(self.root)
        self.root.wait_window(game_option_dialog.dialog)
        game_option, difficulty_level = game_option_dialog.result

        if game_option == "New Game":
            self.start_new_game(difficulty_level)

    def start_new_game(self, difficulty_level):
        """Starts a new game with the specified difficulty level.

        Args:
            difficulty_level: The difficulty level chosen by the user.
        """
        puzzles = self.fetch_puzzles(difficulty_level)
        self.setup_ui(puzzles)


    def fetch_puzzles(self, difficulty):
        """Fetches Sudoku puzzles from the database based on the specified difficulty.

        Args:
            difficulty: The difficulty level of the puzzles to fetch.

        Returns:
            str: A string representing the fetched Sudoku puzzle.
        """
        puzzle = self.db_handler.get_puzzle_by_difficulty(difficulty)
        return puzzle[0]

    def setup_ui(self, puzzles):
        """Sets up the user interface for the Sudoku game.

        Args:
            puzzles: A string representing the Sudoku puzzle to display.
        """
        self.board.initialize_grid(puzzles)

        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)

        self.sudoku_board.update_buttons()

        self.root.geometry("700x700")

    def __del__(self):
        """Destructor method to ensure proper cleanup."""
        self.db_handler.close_connection()
