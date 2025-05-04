import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from core.query import Query
from core.storage import DataStorage
from models.record import Record
from models.user import User

class TestDataStorage(unittest.TestCase):

    def test_add_and_search_record(self):
        record = Record("1", {"name": "datafile1", "type": "json"})
        query = Query("type", "json")
        user = User("u1", "Admin")
        storage = DataStorage()

        user.add_record(record, storage)
        results = user.search_records(query, storage)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].key, "1")

if __name__ == '__main__':
    unittest.main()
