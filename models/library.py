import sqlite3
from models import Book, Status
class My_Library:
    def __init__(self, fname = "library.txt"):
        self.create_table()
        self.fname = fname

    def save_in_file(self):
        conn = sqlite3.connect("my_library.db")
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM books;''')
        result = cursor.fetchall()

    
        with open(self.fname, 'w', encoding='utf-8') as f:
            for row in result:
                book = Book(row[1],row[2],row[3],row[4])
                f.write(str(book) + '\n')
    
    
    def create_table(self):
        conn = sqlite3.connect("my_library.db")
        cursor = conn.cursor()
        create_query = ''' CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL,
        status TEXT NOT NULL CHECK(status IN ('в наличии','выдана')));'''
        try:
            cursor.execute(create_query)
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")
        conn.commit()
        conn.close()

    def add_new_book(self, book: Book):
        conn = sqlite3.connect("my_library.db")
        cursor = conn.cursor()
        new_book = ''' INSERT INTO books(title, author, year, status) VALUES (?, ?, ?, ?);'''
        try:
            cursor.execute(new_book, (book.title, book.author, book.year, 'в наличии'))
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")
        conn.commit()
        conn.close()
        print(f"Книга {book.title} добавлена!")

    def search_book(self, title: str, author: str, year: int) -> list:
        conn = sqlite3.connect("my_library.db")
        cursor = conn.cursor()

        search = '''SELECT * FROM books WHERE title = ? OR author = ? OR year = ?;'''
        try:
            cursor.execute(search, (title, author, year))
            
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")
        
        results = cursor.fetchall()
        if results:
            for result in results:
                print(f"ID: {result[0]} | Название: {result[1]} | Автор: {result[2]} | Год издания: {result[3]} | Статус: {result[4]}")
        else:
            print("Книга не найдена:(")
        conn.close()

    def all_books(self)->list:
        conn = sqlite3.connect("my_library.db")
        cursor = conn.cursor()
        all_query = '''SELECT * FROM books;'''
        try:
            cursor.execute(all_query)
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")
            
        results = cursor.fetchall()
        if results:
            for result in results:
                print(f"ID: {result[0]} | Название книги: {result[1]} | Автор книги: {result[2]} | Год издания: {result[3]} | Статус: {result[4]}")
        else:
            print("Книг нет:(")
    def delete_book(self, id: int):
        conn = sqlite3.connect("my_library.db")
        cursor = conn.cursor()

        delete = '''DELETE FROM books WHERE id = ?; '''
        try:
            cursor.execute(delete, (id,))
            if cursor.rowcount == 0:
                raise ValueError("Книга с таким id не найдена")
            print("Книга удалена")
        except ValueError as ve:
            print(ve)
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")
        conn.commit()
        conn.close()
    def change_status(self, id: int, new_status: Status):
        
        conn = sqlite3.connect("my_library.db")
        cursor = conn.cursor()
        change = '''UPDATE books SET status = ? WHERE id = ?'''
        try:
            cursor.execute(change, (new_status.value, id))
            if cursor.rowcount == 0:
                raise ValueError("Книга не найдена")
            print("Книга удалена")
        except ValueError as ve:
            print(ve)
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")
        conn.commit()
        conn.close()
    def book_report(self):
        self.save_in_file()