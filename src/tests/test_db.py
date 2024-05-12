import unittest
from database import DatabaseHandler
from cell import Cell


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

    def test_serialize_and_insert_and_get_game_state(self):
        last_game_state = [[Cell() for _ in range(9)] for _ in range(9)]

        serialized_state = self.db_handler.serialize_game_state(last_game_state)

        self.db_handler.insert_game_state(serialized_state)

        last_state = self.db_handler.get_last_game_state()

        self.assertIsNotNone(last_state)
        game_is_saved = self.db_handler.has_saved_game()
        self.assertTrue(game_is_saved)


    def test_get_game_state_empty_db(self):
        self.db_handler.clear_game_state_table()
        last_state = self.db_handler.get_last_game_state()

        self.assertIsNone(last_state)
        game_is_saved = self.db_handler.has_saved_game()
        self.assertFalse(game_is_saved)
