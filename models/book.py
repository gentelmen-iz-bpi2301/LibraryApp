import enum

class Status(enum.Enum):
    available = "в наличии"
    expired = "выдана"

class Book:
    def __init__ (self, title, author, year, status=Status):
        self.title = title
        self.author = author
        self.year = year
        self.status = "в наличии"
    
    def __str__(self):
        return f"Название: {self.title} | Автор книги: {self.author} | Год издания: {self.year} | Статус: {self.status}"
    
