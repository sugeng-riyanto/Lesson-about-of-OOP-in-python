
  

# Assessment: Understanding OOP Concepts and Misconceptions

  

---

  

## Quiz: Multiple-Choice Questions on OOP Concepts and Misconceptions

  

1.  **Which of the following is an example of Encapsulation?**

  - (a) Creating a subclass from a parent class.
  
  - (b) Wrapping data and methods into a single unit like a class.
  
  - (c) Using the same interface for different types.
  
  - (d) Hiding implementation details from users.

  

**Answer:** (b) Wrapping data and methods into a single unit like a class.

  

2.  **What is the purpose of the `__init__` method in Python?**

  - (a) It defines a new class.
  
  - (b) It initializes an object and assigns initial values to attributes.
  
  - (c) It deletes an object.
  
  - (d) It is used to inherit attributes from a parent class.

  

**Answer:** (b) It initializes an object and assigns initial values to attributes.

  

3.  **Which of the following best describes Polymorphism?**

  - (a) A single interface that can represent multiple underlying forms.
  
  - (b) Reusing code by inheriting from a parent class.
  
  - (c) Protecting sensitive data by hiding it.
  
  - (d) Wrapping data and methods into a single unit.

  

**Answer:** (a) A single interface that can represent multiple underlying forms.

  

4.  **What will happen if you try to access a private attribute directly?**

  - (a) You will get a syntax error.
  
  - (b) You will get an AttributeError.
  
  - (c) You will access the value without issue.
  
  - (d) The program will terminate unexpectedly.

  

**Answer:** (b) You will get an AttributeError.

  

5.  **Which statement about OOP is incorrect?**

  - (a) OOP is always the best approach for every problem.
  
  - (b) Encapsulation hides the internal implementation details.
  
  - (c) Inheritance allows creating new classes from existing ones.
  
  - (d) Polymorphism enables code reuse and flexibility.

  

**Answer:** (a) OOP is always the best approach for every problem.

  

---

  

## Coding Task: Extend the Library Management System

  

### Task Details:

1. Add a feature to issue a book:

- Mark the book as "Not Available" when issued.

- Provide the name of the person who issued the book.

  

2. Add a feature to return a book:

- Mark the book as "Available" when returned.

  

### Expected Solution:

  
```python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True
        self.issued_to = None

    def issue(self, person):
        if self.is_available:
            self.is_available = False
            self.issued_to = person
            return f"The book '{self.title}' has been issued to {person}."
        else:
            return f"The book '{self.title}' is currently not available."

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            issued_to = self.issued_to
            self.issued_to = None
            return f"The book '{self.title}' has been returned by {issued_to}."
        else:
            return f"The book '{self.title}' is already available."

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            status = "Available" if book.is_available else f"Issued to {book.issued_to}"
            print(f"{book.title} by {book.author} - {status}")

library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)
library.add_book(book2)

# Display initial books
library.display_books()

# Issue and return operations
print(book1.issue("Alice"))
print(book1.issue("Bob"))
print(book1.return_book())
print(book1.issue("Bob"))
library.display_books()
```

  

---

