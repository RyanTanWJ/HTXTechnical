import unittest
from unittest.mock import MagicMock, patch
import sqlite_db

class TestSqliteDb(unittest.TestCase):

    def setUp(self) -> None:
        sqlite_db.engine = None
        return super().setUp()
    
    @patch("sqlite_db.create_engine")
    def test_get_engine(self, create_engine:MagicMock):
        self.assertIsNone(sqlite_db.engine)
        engine = sqlite_db.get_engine()
        self.assertIs(engine, sqlite_db.engine)
        create_engine.assert_called_once()
        
    @patch("sqlite_db.insert")
    def test_write(self, insert:MagicMock):
        sqlite_db.write("a.mp3","t.txt")
        insert.assert_called_once()
        
    @patch("sqlite_db.select")
    def test_get_all(self, select:MagicMock):
        sqlite_db.get_all()
        select.assert_called_once()
        
    @patch("sqlite_db.select")
    def test_search(self, select:MagicMock):
        sqlite_db.search("test search")
        select.assert_called_once()
    

if __name__ == '__main__':
    unittest.main()