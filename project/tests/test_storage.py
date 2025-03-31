import unittest
from unittest.mock import MagicMock
from src.storage import User, Query, DataStorage, Record

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("user123", "John Doe")
        self.storage = DataStorage()
        self.query = Query("name", "John")
        self.record = Record("record1", {"name": "John", "age": 30})

    def test_user_initialization(self):
        self.assertEqual(self.user.get_id(), "user123")
        self.assertEqual(self.user.get_name(), "John Doe")

    def test_search_method(self):
        self.storage.add_record(self.record)
        results = self.user.search(self.query, self.storage)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "John")

class TestDataStorage(unittest.TestCase):
    def setUp(self):
        self.storage = DataStorage()
        self.record = Record("record1", {"name": "John", "age": 30})
        self.query = Query("name", "John")

    def test_add_record(self):
        self.storage.add_record(self.record)
        self.assertIn("record1", self.storage._storage)

    def test_delete_record(self):
        self.storage.add_record(self.record)
        self.storage.delete_record("record1")
        self.assertNotIn("record1", self.storage._storage)

    def test_delete_nonexistent_record(self):
        with self.assertRaises(KeyError):
            self.storage.delete_record("nonexistent")

    def test_search(self):
        self.storage.add_record(self.record)
        results = self.storage.search(self.query)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "John")

    def test_search_no_results(self):
        empty_query = Query("name", "NonExistent")
        results = self.storage.search(empty_query)
        self.assertEqual(len(results), 0)

if __name__ == "__main__":
    unittest.main()
