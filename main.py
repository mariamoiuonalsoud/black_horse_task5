from lms import Book, Member, StaffMember, Library

if __name__ == "__main__":
    
    library = Library()

    staff = StaffMember("Sarah", "M001", "S100")
    staff.add_book(library, "The Alchemist", "Paulo Coelho", "9780061122415")
    staff.add_book(library, "1984", "George Orwell", "9780451524935")

   
    library.show_books()

 
    member = Member("Omar", "M002")


    member.borrow_book(library.books[0])
    member.return_book(library.books[0])

    print("\nMember ID:", member.get_membership_id())
    print("Book ISBN:", library.books[0].get_isbn())