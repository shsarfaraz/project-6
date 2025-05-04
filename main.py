# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. 
# Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        return(f'Name: {self.name}, "Marks:", {self.marks}') 
      

student1: Student = Student("Sarfaraz", 90)
student2: Student = Student("Ali", 80)
print ("Student 1 details:" , student1.display())
print(student1.name, student1.marks)
print ("Student 2 details:" , student2.display())


# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def display_count(cls):
        return f'Total objects created: {cls.count}'
    
counter1: Counter = Counter()
counter2: Counter = Counter()
counter3: Counter = Counter()
print(Counter.display_count())


# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f'The {self.brand} has started')

car1: Car = Car("Honda")
car1.start()


# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "ABC Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

b1: Bank = Bank()
print(b1.bank_name)
b2: Bank = Bank()
print(b2.bank_name)
Bank.change_bank_name("XYZ Bank")
print(b1.bank_name)
print(b2.bank_name)

# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
print(MathUtils.add(2, 3))

# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Object created")

    # def __del__(self):
    #     print("Object destroyed")

logger1: Logger = Logger()



# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

    def display(self):
        return(f'Name: {self.name}, "Salary:", {self._salary}, "SSN:", {self.__ssn}')
    
employee1: Employee = Employee("Sarfaraz", 100000, 123456789)
print(employee1.display())
print(employee1._Employee__ssn)
print(employee1._salary)


# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and 
# use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

teacher1: Teacher = Teacher("Sarfaraz", "Python")
print(f'Name: {teacher1.name}, Subject: {teacher1.subject}')


# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass    

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rectangle1: Rectangle = Rectangle(10, 5)
print(f'Area of Rectangle: {rectangle1.area()}')


# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return(f'{self.name} barks')

dog1: Dog = Dog("Buddy", "Labrador")
print(dog1.bark())


# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self, title):
        self.title = title
        Book.total_books += 1

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1

book1: Book = Book("The Great Gatsby")
book2: Book = Book("To Kill a Mockingbird")
print(f'Total books: {Book.total_books}')   

Book.increment_book_count()
print(f'Total books: {Book.total_books}')

# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C is equal to {temp_f}°F")


# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self, engine):
        self.engine = engine  

    def start_car(self):
        return self.engine.start()  


my_engine = Engine()
my_car = Car(my_engine)
print(my_car.start_car())  

# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee Name: {self.name}"


class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee  

    def get_department_info(self):
        return f"Department: {self.name}, {self.employee.get_details()}"


emp = Employee("Sarfaraz Ahmed")         
dept = Department("HR", emp)    

print(dept.get_department_info())



# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


class A:
    def show(self):
        return "Show from A"

class B(A):
    def show(self):
        return "Show from B"

class C(A):
    def show(self):
        return "Show from C"

class D(B, C):  
    pass

d = D()
print(d.show()) 
print(D.__mro__)


# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello(name):    
    return f"Hello, {name}"

print(say_hello("Sarfaraz"))


# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls

@add_greeting
class Person:
    pass

person1: Person = Person()
print(person1.greet())


# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        del self._price

product1: Product = Product(100)
print(product1.price)

product1.price = 200
print(product1.price)

del product1.price



# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.


class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, num):
        return num * self.factor

multiplier1: Multiplier = Multiplier(2)
print(multiplier1(5))
print(callable(multiplier1))



# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.


class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Must be 18 or older.")

try:
    check_age(15)
except InvalidAgeError as e:
    print(e)



# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        value = self.start
        self.start -= 1
        return value

countdown = Countdown(5)
for num in countdown:
    print(num)