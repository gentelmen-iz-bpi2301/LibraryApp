import unittest
import os

from models import Book, My_Library, Status

class TestLibrary(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.db_name = 'test_library.db'
        cls.text_file_name = 'test_library.txt'
        
    @classmethod
    def tearDownClass(cls):

        if os.path.exists(cls.db_name):
            os.remove(cls.db_name)
        if os.path.exists(cls.text_file_name):
            os.remove(cls.text_file_name)

    def setUp(self):
        self.library = My_Library(db_name=self.db_name, fname=self.text_file_name)

    def test_add_book(self):

        self.library.add_new_book(book = Book("Test Book", "Test Author", 2023, 'в наличии'))

        found_book = None
        for book in self.library.cursor.execute('SELECT * FROM books'):
            if book[1] == "Test Book":
                found_book = book

        self.assertIsNotNone(found_book)
        self.assertEqual(found_book[2], "Test Author")

    def test_delete_book(self):
        self.library.add_new_book(book = Book("Book to Remove", "Test Author", 2023, 'в наличии'))

        
        removed_book_id = None
        for book in self.library.cursor.execute('SELECT * FROM books'):
            if book[1] == "Book to Remove":
                removed_book_id = book[0]

        self.library.delete_book(removed_book_id)
        found_removed_book = next((b for b in self.library.cursor.execute('SELECT * FROM books') if b[0] == removed_book_id), None)

        self.assertIsNone(found_removed_book)

    def test_search_book(self):
        
        self.library.add_new_book(book = Book("Searchable Book", "Search Author", 2023, 'в наличии'))

        results = []
        for book in self.library.cursor.execute('SELECT * FROM books WHERE title LIKE ?', ('%Searchable Book%',)):
            results.append(book)
        self.assertGreater(len(results), 0)

    def test_change_status(self):
        
        self.library.add_new_book(book = Book("Status Change Book", "Author", 2023, 'в наличии'))
        
        
        added_book_id = None
        for book in self.library.cursor.execute('SELECT * FROM books'):
            if book[1] == "Status Change Book":
                added_book_id = book[0]

        self.library.change_status(added_book_id, Status.expired)

        updated_book = next(b for b in self.library.cursor.execute('SELECT * FROM books') if b[0] == added_book_id)

        self.assertEqual(updated_book[4], 'выдана')

if __name__ == '__main__':
    unittest.main()