import tkinter as tk


class GameStartDialog:
    """Object that handles the starting dialog for the Sudoku game.
    Attributes:
        parent (root): The main frame window
        sudoku_game_manager: An instance of SudokuGameManager class
        message (str): a message that is shown when the game is completed.
        """

    def __init__(self, parent, sudoku_game_manager, message=None):
        self.parent = parent
        self.sudoku_game_manager = sudoku_game_manager
        self.result = None

        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Select Option")
        self.dialog.transient(parent)
        self.dialog.geometry("450x300")

        self.create_widgets()
        if message:
            self.show_message(message)

        self.check_saved_game()


    def create_widgets(self):
        """Create widgets for the game selection."""

        tk.Label(self.dialog, text="Choose Option:").pack()

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

        self.continue_game_button = tk.Button(
            self.dialog,
            text="Continue Game",
            command=self.continue_game,
            state=tk.DISABLED,
        )
        self.continue_game_button.pack()

        self.restart_button = tk.Button(
            self.dialog, text="Restart", command=self.restart, state=tk.DISABLED
        )
        self.restart_button.pack()

    def show_message(self, message):
        """Show message when the game is completed."""

        tk.Label(self.dialog, text=message).pack()

    def check_saved_game(self):
        """Check if there is a saved game in the database."""
        saved_game_exists = self.sudoku_game_manager.db_handler.has_saved_game()
        if saved_game_exists:
            self.continue_game_button.config(state=tk.NORMAL)
            self.restart_button.config(state=tk.NORMAL)

    def new_game(self):
        """Start new game with selected difficulty"""

        selected_difficulty = self.difficulty_var.get()
        self.result = ("New Game", selected_difficulty)
        self.sudoku_game_manager.start_new_game(selected_difficulty)
        self.dialog.destroy()

    def continue_game(self):
        """Continue previous game"""

        self.result = ("Continue Game", None)
        self.sudoku_game_manager.continue_game()
        self.dialog.destroy()

    def restart(self):
        """Restart previous game"""

        self.result = ("Restart", None)
        self.sudoku_game_manager.restart_game()
        self.dialog.destroy()
