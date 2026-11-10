import unittest

from main import sqlite_demo, orm_crud_demo


class DatabaseTests(unittest.TestCase):
    def test_sqlite(self):
        self.assertEqual(sqlite_demo(), [("Шкловский Герман", "221141")])

    def test_orm(self):
        result = orm_crud_demo()
        self.assertEqual(result["read"], "Герман")
        self.assertEqual(result["updated"], "Шкловский Герман")
        self.assertTrue(result["deleted"])


if __name__ == "__main__":
    unittest.main()
