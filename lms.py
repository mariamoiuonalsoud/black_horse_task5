class Library:
    def __init__(self):
        self.books = []
    def show_books(self):
        if not self.books:
            print("There are no books in the library!")
        else:
            print("Library Books:")
            for book in self.books:
                book.display_info()

class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author= author
        self.__isbn = isbn
        self.available = available
    
    def get_isbn(self):
        return self.__isbn
    

    def set_isdn(self, new_isbn):
        self.__isbn = new_isbn


    def display_info(self):
        print("### Book Info ###")
        print(f"Book Title: {self.title}\n Book Author: {self.author}\n Book ISBN: {self.__isbn}\n Book Availablilty: {self.available}")


class Member:
    def __init__(self, name, membership_id, borrowed_books = None):
        self.name = name
        self.__membership_id = membership_id
        self.borrowed_books= borrowed_books if borrowed_books is not None else []
    
    def get_membership_id(self):
        return self.__membership_id
    
    def set_membership_id(self, new_membership_id):
        self.__membership_id = new_membership_id

    def borrow_book(self, book):
        if book.available:
            self.borrowed_books.append(book)
            book.available = False
            print(f"{self.name} borrowed '{book.title}'.")
        else:
            print(f"Sorry, {book.title} is not available!")
    
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.available = True
            print(f"{self.name} returned '{book.title}'.")
        else:
            print(f"{self.name} does not have '{book.title}' borrowed.")

class StaffMember(Member):
    def __init__(self,name,membership_id, staff_id):
        super().__init__(name, membership_id)
        self.staff_id= staff_id
    
    def add_book(self, library, title, author, isbn):
        new_book = Book(title, author, isbn)
        library.books.append(new_book)
        print(f"{new_book} added to {library}!")

        


if __name__ == "__main__":
    print("Library Management System classes loaded successfully!")
