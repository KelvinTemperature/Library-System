# Smart Library System 📚

## 📌 Project Overview

The Smart Library System is a Python-based application designed to manage books within a digital library environment without relying on an external database.

This system demonstrates advanced Python concepts such as:

- Object-Oriented Programming (OOP)
- Magic Methods (Dunder Methods)
- Decorators
- Closures
- Duck Typing
- Python Packaging
- Method Resolution Order (MRO)

---

## 🧱 Project Structure

library_system/
│
├── __init__.py
├── core.py
├── utils.py
└── __main__.py


---

## ⚙️ Features Implemented

### 1. Book Class
- `__str__()` → Provides user-friendly book representation  
- `__len__()` → Returns the number of pages  
- `__eq__()` → Compares books based on title and author  

### 2. Library Class
- Stores and manages books
- Iterable using `__getitem__()`
- Supports:
  - Adding books
  - Borrowing books
  - Returning books

---

## 🛡️ Decorators & Closures

### Logging Decorator

The `@track_access` decorator logs:
- Method name
- Arguments
- Timestamp

whenever a book is borrowed or returned.

---

### Access Control Using Closures

The `permission_check(required_role)` closure restricts access to certain methods such as:

```python
@permission_check("Admin")
def add_book(self, user, book):

🦆 Duck Typing Implementation

The system supports duck typing through the borrow_item(item) function.

Any object passed into this function will work as long as it has a .title attribute, regardless of its class type.

This demonstrates Python’s dynamic typing philosophy:
"If it walks like a duck and quacks like a duck, it is a duck."

### 🧬 Method Resolution Order (MRO) Analysis

If a DigitalBook class inherits from both Book and a hypothetical Software class:

class DigitalBook(Book, Software):
    pass

Python determines the Method Resolution Order (MRO) using the C3 Linearization algorithm.

Calling:

DigitalBook.mro()

returns:

[DigitalBook, Book, Software, object]

This means that when a method is called on a DigitalBook instance, Python searches for the method in the following order:

DigitalBook

Book

Software

object

For example, if both Book and Software define an open() method, Python will resolve the method from the Book class first because it appears before Software in the inheritance list.

This guarantees a consistent and predictable method lookup order and avoids ambiguity in multiple inheritance scenarios.

### ▶️ How to Run the Application

From the project root directory, run:

python -m library_system

### 📚 Technologies Used

Python 3.x
