import unittest
from database import DatabaseHandler


class TestDatabaseHandler(unittest.TestCase):
    def setUp(self):
        self.db_handler = DatabaseHandler(":memory:")
        self.db_handler.create_table()

    def tearDown(self):
        self.db_handler.close_connection()

    def test_insert_and_fetch_puzzle(self):
        puzzle = (
            "530070000600195000098000060800060003400803001700020006060000280000419005000080079",
            "easy",
        )
        self.db_handler.insert_puzzle(puzzle[0], puzzle[1])
        inserted_puzzle = self.db_handler.get_all_puzzles()
        self.assertIsNotNone(inserted_puzzle)

        fetched_puzzle = self.db_handler.get_puzzle_by_difficulty("easy")
        self.assertIsNotNone(fetched_puzzle)
        self.assertEqual(
            fetched_puzzle,
            (
                "530070000600195000098000060800060003400803001700020006060000280000419005000080079",
            ),
        )

