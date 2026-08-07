class Book:
    def __init__(self,title,category):
        self.title = title
        self.category = category
        self.borrowed = False

    def borrow(self):
        if self.borrowed:
            print(f" Someone {self.title} book already borrowed ")
        else:
            self.borrowed = True
            print(f"You can now take {self.title} book")

    def return_book(self):
        if self.borrowed:
            print(f" You have returned {self.title} book ")
        else:
            self.borrowed = False
            print(f"{self.title} is already returned ")

    def show_book(self):
        print(f"Title: {self.title}")
        print(f"Category: {self.category}")
        if self.borrowed:
            print(f"Status: Not available")
        else:
            print(f"Status: Available")

# class Library:
#     def __init__(self):
#         # self.book_title = book_title
#         # self.book_author = book_author
#         # self.book_genre = book_genre
#         # self.book_pages = book_pages
#         # self.borrowed = borrowed
#         self.book_list = ["RDPD","Big Bang"]
#
#     def add_book(self, book_name):
#         self.book_list.append(book_name)
#         print(f"{book_name} added to library, available books {self.book_list}")
#
#     def remove_book(self, book_name):
#         self.book_list.remove(book_name)
#
#     def show_book_list(self):
#         for book in  self.book_list:
#             print(f"you have these books available:{book}")
#
#     def borrow_book(self, book_name):
#         self.book_list.remove(book_name)
#         print(f"{book_name} borrowed, remaining books {self.book_list}")
#
#     def return_book_list(self,book_name):
#         print(f"You have returned {book_name}")
#         self.book_list.append(book_name)
#         print(f"{self.book_list}")