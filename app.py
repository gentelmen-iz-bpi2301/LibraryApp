
from models import Book, Status, My_Library

class App:
    def __init__(self):
        self.library = My_Library()

    def run(self):
        while True:
            print("\Меню")
            print("1. Добавить книгу")
            print("2. Найти книгу")
            print("3. Показать все книги")
            print("4. Удалить книгу")
            print("5. Изменить статус")
            print("6. Отчёт")
            print("7. Выход")


            activity = input("Выберите действие(укажите цифру от 1 до 7): ")

            if activity=="1":
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = input("Введите год издания: ")
                book = Book(title, author, year)
                self.library.add_new_book(book)
            elif activity =="2":
                title = input("Введите название книги, которую хоите найти: ")
                author = input("Укажите автора книги, которую хотите найти: ")
                year = input("Укажите год издания книги, которую хотите найти: ")
                self.library.search_book(title, author, year)
            elif activity=="3":
                self.library.all_books()
            elif activity == "4":
                id = input("Введите id книги, которую нужно удалить: ")
                self.library.delete_book(id)
            elif activity == "5":
                id = input("Введите id книги, статус которой нужно изменить: ")
                new_status = input("Выберите новый статус: 1.В наличии, 2. Выдана: ")
                if new_status == "1":
                    new_status = Status.available
                elif new_status == "2":
                    new_status = Status.expired
                else:
                    print("Неверная команда. Выберите 1 или 2 в зависимости от нужного статуса")
                self.library.change_status(id, new_status)
            elif activity =="6":
                self.library.book_report()
                print("Отчёт об имеющихся книгах находится в файле 'library.txt")
            elif activity == "7":
                print("Завершение работы")
                break
            else:
                print("Неверный номер команды. Выберите циыру от 1 до 7 в зависимости от действия.")

if __name__ == "__main__":
    app = App()
    app.run()
