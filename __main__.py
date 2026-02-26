from .core import Book, Library, User


class Magazine:
        def __init__(self, title):
            self.title = title
            
            
def main():
    library = Library()

    admin = User("Kelvin", "Admin")
    member = User("John", "Member")

    book1 = Book("Atomic Habits", "James Clear", 320)
    book2 = Book("Deep Work", "Cal Newport", 296)

    # Admin adds books
    print("\n--- Admin Adding Books ---")
    library.add_book(admin, book1)
    library.add_book(admin, book2)

    # Member tries to add book
    print("\n--- Member Trying to Add Book ---")
    try:
        library.add_book(member, book1)
    except PermissionError as e:
        print(e)

    # Borrow book
    print("\n--- Borrowing Book ---")
    library.borrow_book(book1)

    # Return book
    print("\n--- Returning Book ---")
    library.return_book(book1)

    # Iterate through library
    print("\n--- Library Collection ---")
    for book in library:
        print(book)
        
    print("\n--- Duck Typing Test ---")

    mag = Magazine("Tech Monthly")
    library.borrow_item(mag)


if __name__ == "__main__":
    main()