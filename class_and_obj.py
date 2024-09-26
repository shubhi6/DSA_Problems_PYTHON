# 1. Define a python class Person with instance object variables name and age. Set Instance object variables in init_() method. Also define show() method to display name and age of a person.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")
name = input("Enter name: ")
age = int(input("Enter age: "))
person = Person(name, age)
person.show()

# 2. Define a class Circle with instance object variable radius. Provide setter and getter for radius. Also define getArea() and getCircumference() methods.
class Circle:
    def __init__(self, radius=0):
        self._radius = radius

    def setRadius(self, radius):
        self._radius = radius

    def getRadius(self):
        return self._radius

    def getArea(self):
        return 3.14159 * self._radius ** 2

    def getCircumference(self):
        return 2 * 3.14159 * self._radius
radius = float(input("Enter radius: "))
circle = Circle()
circle.setRadius(radius)
print(f"Radius: {circle.getRadius()}")
print(f"Area: {circle.getArea()}")
print(f"Circumference: {circle.getCircumference()}")

# 3. Define a class Rectangle with length and breadth as instance object variables. Provide setDimensions(), showDimensions() and getArea() method in it.
class Rectangle:
    def __init__(self, length=0, breadth=0):
        self.length = length
        self.breadth = breadth

    def setDimensions(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def showDimensions(self):
        print(f"Length: {self.length}, Breadth: {self.breadth}")

    def getArea(self):
        return self.length * self.breadth
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
rectangle = Rectangle()
rectangle.setDimensions(length, breadth)
rectangle.showDimensions()
print(f"Area: {rectangle.getArea()}")

# 4. Define a class Book with instance object variables bookid, title and price. Initialise them via_init_() method. Also define method to show book variables.
class Book:
    def __init__(self, bookid, title, price):
        self.bookid = bookid
        self.title = title
        self.price = price

    def show(self):
        print(f"Book ID: {self.bookid}, Title: {self.title}, Price: {self.price}")
bookid = input("Enter book ID: ")
title = input("Enter book title: ")
price = float(input("Enter price: "))
book = Book(bookid, title, price)
book.show()

# 5. Define a class Team with instance object variable a list of team member names.
class Team:
    def __init__(self):
        self.members = []

    def inputMembers(self, *names):
        self.members.extend(names)

    def displayMembers(self):
        for member in self.members:
            print(member)
team = Team()
members = input("Enter team members' names, separated by space: ").split()
team.inputMembers(*members)
team.displayMembers()
