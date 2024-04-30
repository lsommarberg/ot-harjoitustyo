import sqlite3


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

    def close_connection(self):
        """Closes the connection to the SQLite database."""
        self.conn.close()
