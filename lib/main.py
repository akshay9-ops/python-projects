from book import Book
from library import Library
book = Book("harry potter", "horror")
book1 = Book("python", "study")
# book.borrow()
# book.borrow()
# book.return_book()
# book.borrow()
library = Library()
library.add_book(book)
library.add_book(book1)
library.show_books()

library.borrow_book("python")
library.return_book("python")