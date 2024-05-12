from database import DatabaseHandler
from puzzles import initial_puzzles


class SudokuGameManager:
    """Manages the Sudoku game's core functionalities.

    This class coordinates interactions between the game board, UI components,
    and game logic.

    Attributes:
        board (Board): The game board containing the Sudoku grid.
        db_handler (DatabaseHandler): The handler for interacting with the puzzle database.
        sudoku_board_ui (SudokuBoard): The user interface component
                                        responsible for rendering the Sudoku board.
        game_logic (GameLogic): The logic component responsible for enforcing Sudoku rules
                                 and game mechanics.
    """

    def __init__(self, board, sudoku_board_ui, game_logic):
        self.board = board
        db_file = "sudoku.db"
        self.db_handler = DatabaseHandler(db_file)
        self.sudoku_board_ui = sudoku_board_ui
        self.game_logic = game_logic

        self.initialize_with_default_puzzles()

    def save_game_state(self):
        """
        Save the current state of the Sudoku game, if the game is not completed.

        This function serializes the current game state and saves it to the database.
        """
        if not self.board.is_game_completed:
            current_state = self.board.get_board_state()
            serialized_game_state = self.db_handler.serialize_game_state(current_state)
            self.db_handler.insert_game_state(serialized_game_state)

    def clear_game_state(self):
        """
        Clear game state after a completed game.

        """
        self.board.clear_grid()
        self.game_logic.clear_undo_stack()
        self.board.game_is_not_completed()
        self.clear_states_in_db()

    def clear_states_in_db(self):
        """Clear the game state."""
        self.db_handler.clear_game_state_table()

    def initialize_with_default_puzzles(self):
        """
        Initialize the game with default puzzles.

        This function populates the game with a set of default Sudoku puzzles.
        """
        for puzzle_info in initial_puzzles:
            puzzle = puzzle_info["Puzzle"]
            difficulty = puzzle_info["Difficulty"]

            self.db_handler.insert_puzzle(puzzle, difficulty)

    def fetch_puzzle(self, difficulty):
        """
        Fetch puzzle with given difficulty level from the database.

        Args:
            difficulty_level (str): The difficulty level of the new game:
            ('Easy', 'Medium', or 'Hard').
        """
        puzzle = self.db_handler.get_puzzle_by_difficulty(difficulty)
        return puzzle[0]

    def start_new_game(self, difficulty_level):
        """
        Start a new game with the specified difficulty level.

        Args:
            difficulty_level (str): The difficulty level of the new game:
            ('Easy', 'Medium', or 'Hard').
        """
        self.board.clear_grid()
        puzzles = self.fetch_puzzle(difficulty_level)
        self.board.initialize_grid(puzzles)
        self.sudoku_board_ui.update_buttons()

    def continue_game(self):
        """
        Continue the last saved game.

        This function retrieves the last saved game state from the database and resumes the game.
        """
        self.board.clear_grid()

        game_state = self.db_handler.get_last_game_state()

        self.board.grid = game_state
        self.sudoku_board_ui.update_buttons()

    def restart_game(self):
        """
        Restart the current game.

        This function resets the current game to its initial state,
        preserving the game's difficulty level.
        """
        self.board.clear_grid()
        self.game_logic.clear_undo_stack()
        restart_game_state = self.initialize_grid_for_restart()
        self.board.initialize_grid(restart_game_state)
        self.sudoku_board_ui.update_buttons()

    def initialize_grid_for_restart(self):
        """
        Initialize the grid for game restart.

        This function prepares the game grid for a restart by clearing cells with user inputs.
        """
        last_game_state = self.db_handler.get_last_game_state()
        restart_game_state = ""

        for row in range(9):
            for col in range(9):
                cell = last_game_state[row][col]
                if cell.is_locked:
                    restart_game_state += str(cell.get_value())
                else:
                    restart_game_state += "0"
        return restart_game_state

    def close(self):
        self.db_handler.close_connection()
