#mFinish the Library project.

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def show_books(self):
        for book in self.book_list:
            book.show_book()
            print("\n")

    def borrow_book(self, title):
        for book in self.book_list:
            if title == book.title:
                book.borrow()

    def return_book(self,title):
        for book in self.book_list:
            if title == book.title:
                book.return_book()