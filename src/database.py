import sqlite3
import json
from cell import Cell


class DatabaseHandler:
    """Handles interactions with the SQLite database for Sudoku puzzles.

    This class provides methods to create tables, insert puzzles into the database,
    retrieve puzzles by difficulty level, retrieve all puzzles, and close the database connection.

    Attributes:
        db_file (str): The file path of the SQLite database.

    """

    def __init__(self, db_file):
        """Constructor for the DatabaseHandler class.

        Initializes the DatabaseHandler with the SQLite database file specified by `db_file`.
        It also creates the necessary table if it does not already exist.

        Args:
            db_file (str): The file path of the SQLite database.

        """
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the 'puzzles' table in the database if it does not already exist.

        The 'puzzles' table is used to store Sudoku puzzles, where each puzzle
        is associated with a difficulty level.

        """
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS puzzles (
                id INTEGER PRIMARY KEY,
                puzzle TEXT NOT NULL,
                difficulty TEXT
            )
        """
        )
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS game_states (
                id INTEGER PRIMARY KEY,
                state TEXT NOT NULL
            )
            """
        )
        self.conn.commit()

    def insert_puzzle(self, puzzle, difficulty):
        """Inserts a Sudoku puzzle into the 'puzzles' table of the database.

        Args:
            puzzle (str): The Sudoku puzzle as a string.
            difficulty (str): The difficulty level of the puzzle.

        """
        self.cursor.execute(
            """
            INSERT INTO puzzles (puzzle, difficulty)
            VALUES (?, ?)
        """,
            (puzzle, difficulty),
        )
        self.conn.commit()

    def get_puzzle_by_difficulty(self, difficulty):
        """Retrieves a random Sudoku puzzle from the database based on the specified
        difficulty level.

        Args:
            difficulty (str): The difficulty level of the puzzle to retrieve.

        Returns:
            tuple: A tuple containing the puzzle string.

        """
        self.cursor.execute(
            """
            SELECT puzzle FROM puzzles WHERE difficulty = ? ORDER BY RANDOM() LIMIT 1
        """,
            (difficulty,),
        )
        return self.cursor.fetchone()

    def get_all_puzzles(self):
        """Retrieves all Sudoku puzzles from the database.

        Returns:
            list: A list of tuples, where each tuple contains the puzzle string
            and its associated difficulty level.

        """
        self.cursor.execute("SELECT * FROM puzzles")
        return self.cursor.fetchall()

    def get_last_game_state(self):
        """Retrieves the state of the last game from the database.

        Returns:
            list of cell objects: deserialized game state

        """
        try:
            self.cursor.execute(
                """
                SELECT state FROM game_states ORDER BY id DESC LIMIT 1
                """
            )
            serialized_state = self.cursor.fetchone()
            if serialized_state:
                return self.deserialize_game_state(serialized_state[0])
            return None
        except sqlite3.Error as e:
            print("Error fetching game state:", e)
            return None

    def serialize_game_state(self, grid_copy):
        """
        Serialize the game state data (grid_copy) into JSON format.
        """
        serialized_grid = []
        for row in grid_copy:
            serialized_row = []
            for cell in row:
                serialized_cell = {
                    "value": cell.value,
                    "notes": cell.notes,
                    "is_locked": cell.is_locked,
                    "display_notes": cell.display_notes,
                    "value_is_valid": cell.value_is_valid,
                }
                serialized_row.append(serialized_cell)
            serialized_grid.append(serialized_row)

        return json.dumps(serialized_grid)

    def deserialize_game_state(self, serialized_data):
        """
        Deserialize the serialized game state data into a grid structure.
        """
        grid_copy = []
        serialized_grid = json.loads(serialized_data)
        for serialized_row in serialized_grid:
            row = []
            for serialized_cell in serialized_row:
                cell = Cell()
                cell.value = serialized_cell["value"]
                cell.notes = serialized_cell["notes"]
                cell.is_locked = serialized_cell["is_locked"]
                cell.display_notes = serialized_cell["display_notes"]
                cell.value_is_valid = serialized_cell["value_is_valid"]
                row.append(cell)
            grid_copy.append(row)

        return grid_copy

    def has_saved_game(self):
        self.cursor.execute("SELECT * FROM game_states")
        return self.cursor.fetchone() is not None

    def insert_game_state(self, serialized_state):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM game_states")
            count = self.cursor.fetchone()[0]

            if count == 0:
                self.cursor.execute(
                    "INSERT INTO game_states (state) VALUES (?)", (serialized_state,)
                )
            else:
                self.cursor.execute(
                    "UPDATE game_states SET state = ?", (serialized_state,)
                )

            self.conn.commit()

        except sqlite3.Error as e:
            print("Error inserting/updating game state:", e)

    def clear_game_state_table(self):
        """Clears the game state table by deleting all rows."""
        try:
            self.cursor.execute("DELETE FROM game_states")
            self.conn.commit()
        except sqlite3.Error as e:
            print("Error clearing game state table:", e)

    def close_connection(self):
        """Closes the connection to the SQLite database."""
        self.conn.close()
