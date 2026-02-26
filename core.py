from .utils import track_access, permission_check


class Book:
    """
    Represents a book in the smart library system.
    """

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        """
        User-friendly string representation of the book.
        """
        return f"{self.title} by {self.author}"

    def __len__(self) -> int:
        """
        Returns the number of pages in the book.
        """
        return self.pages

    def __eq__(self, other) -> bool:
        """
        Compares two books based on title and author.
        """
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author


class Library:
    """
    Represents a collection of books.
    """

    def __init__(self):
        self._books = []

    # def add_book(self, book: Book):
    #     """
    #     Adds a book to the library.
    #     """
    #     self._books.append(book)

    def remove_book(self, book: Book):
        """
        Removes a book from the library.
        """
        if book in self._books:
            self._books.remove(book)

    def __getitem__(self, index):
        """
        Makes the library iterable.
        """
        return self._books[index]

    def __len__(self):
        """
        Returns total number of books in the library.
        """
        return len(self._books)
    
    @track_access
    def borrow_book(self, book):
        if book in self._books:
            self._books.remove(book)
            print(f"{book.title} has been borrowed.")
        else:
            print("Book not available.")


    @track_access
    def return_book(self, book):
        self._books.append(book)
        print(f"{book.title} has been returned.")


    @permission_check("Admin")
    def add_book(self, user, book):
        self._books.append(book)
        print(f"{book.title} added by {user.name}.")
        
    def borrow_item(self, item):
        """
        Demonstrates duck typing.
        Accepts any object with a .title attribute.
        """
        if hasattr(item, "title"):
            print(f"{item.title} has been borrowed successfully.")
        else:
            raise AttributeError(
                "Item must have a 'title' attribute to be borrowed."
            )

class User:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
    