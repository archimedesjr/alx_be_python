class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author
    self._is_checked_out = "Private Attribute"

class Library(Book):
  def __init__(self):
    self._books = "Private Attribute"
  
  def add_book(self):
    pass

  def check_out_book(self, title):
    pass

  def return_book(self, title):
    pass

  def list_available_books(self, title):
    pass