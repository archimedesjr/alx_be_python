class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = False

class Library:
  def __init__(self):
    self._books = []

  def add_book(self, book):
    self._books.append(book)
  
  def list_available_books(self):
    for book in self._books:
      print(f"{book.title} by {book.author}")

  def check_out_book(self, title):
    for book in self._books:
      if book.title == title:
        self._books.remove(book)
      print(f"{book.title} by {book.author}")
      self._is_checked_out = True
        
  def return_book(self):
    self._is_checked_out = False
    for book in self._books:
      if book.title == title:
        self.books.append(book)
      print(f"{book.title} by {book.author}")