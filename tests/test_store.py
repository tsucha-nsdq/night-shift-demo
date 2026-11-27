import tempfile
import unittest
from pathlib import Path

from bookmemo.store import Book, Store


class StoreTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.store = Store(Path(self.dir.name) / "books.json")

    def tearDown(self):
        self.dir.cleanup()

    def test_empty(self):
        self.assertEqual(self.store.load(), [])

    def test_add_and_load(self):
        self.store.add(Book("コンビニ人間", "村田沙耶香", 4))
        self.assertEqual(self.store.load(), [Book("コンビニ人間", "村田沙耶香", 4)])

    def test_rating_out_of_range(self):
        with self.assertRaises(ValueError):
            self.store.add(Book("x", rating=6))

    def test_delete(self):
        self.store.add(Book("コンビニ人間", "村田沙耶香", 4))
        self.store.add(Book("推し、燃ゆ", "宇佐見りん", 5))
        self.assertEqual(self.store.delete("コンビニ人間"), 1)
        self.assertEqual(self.store.load(), [Book("推し、燃ゆ", "宇佐見りん", 5)])

    def test_delete_duplicates(self):
        self.store.add(Book("x"))
        self.store.add(Book("x", rating=3))
        self.assertEqual(self.store.delete("x"), 2)
        self.assertEqual(self.store.load(), [])

    def test_delete_missing(self):
        self.assertEqual(self.store.delete("ない本"), 0)
        self.assertFalse(self.store.path.exists())


if __name__ == "__main__":
    unittest.main()
