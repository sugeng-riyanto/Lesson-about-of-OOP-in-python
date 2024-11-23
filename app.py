
# app.py: Python Examples from OOP Lesson Plan

# Example 1: Class and Object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

# Creating an object
student1 = Student("Alice", 16)
print(student1.greet())


# Example 2: Encapsulation
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount("Bob", 1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500


# Example 3: Inheritance
class Animal:
    def speak(self):
        return "I make a sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

dog = Dog()
print(dog.speak())  # Output: Woof!


# Example 4: Polymorphism
class Bird:
    def fly(self):
        return "Flying high"

class Penguin(Bird):
    def fly(self):
        return "I can't fly, but I can swim!"

birds = [Bird(), Penguin()]
for bird in birds:
    print(bird.fly())


# Example 5: Debugging Encapsulation Error
class Car:
    def __init__(self, speed):
        self.__speed = speed

    def get_speed(self):
        return self.__speed

my_car = Car(120)
print(my_car.get_speed())


# Example 6: Library Management System
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            status = "Available" if book.is_available else "Not Available"
            print(f"{book.title} by {book.author} - {status}")

library = Library()
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)
library.add_book(book2)
library.display_books()
