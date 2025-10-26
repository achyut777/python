"""
Python Basics - A Comprehensive Guide
This file covers all fundamental concepts in Python
"""

# ============================================================================
# 1. COMMENTS AND DOCUMENTATION
# ============================================================================

# This is a single-line commen

"""
This is a multi-line comment
or docstring used for documentation
"""

# ============================================================================
# 2. VARIABLES AND DATA TYPES
# ============================================================================

# Integer
age = 25
print(f"Integer: {age}, Type: {type(age)}")

# Float
price = 19.99
print(f"Float: {price}, Type: {type(price)}")

# String
name = "Python"
message = 'Hello, World!'
print(f"String: {name}, Type: {type(name)}")

# Boolean
is_active = True
is_valid = False
print(f"Boolean: {is_active}, Type: {type(is_active)}")

# None Type
empty_value = None
print(f"None: {empty_value}, Type: {type(empty_value)}")

# ============================================================================
# 3. STRING OPERATIONS
# ============================================================================

# String concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"Full Name: {full_name}")

# String formatting
age = 30
formatted_string = f"My name is {full_name} and I am {age} years old"
print(formatted_string)

# String methods
text = "  Python Programming  "
print(f"Original: '{text}'")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Strip: '{text.strip()}'")
print(f"Replace: {text.replace('Python', 'Java')}")
print(f"Split: {text.split()}")

# String slicing
word = "Python"
print(f"First character: {word[0]}")
print(f"Last character: {word[-1]}")
print(f"First 3 characters: {word[0:3]}")
print(f"From index 2: {word[2:]}")
print(f"Reverse: {word[::-1]}")

# ============================================================================
# 4. LISTS (Ordered, Mutable)
# ============================================================================

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]

print(f"Fruits: {fruits}")

# List operations
fruits.append("orange")          # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "mango")        # Insert at index
print(f"After insert: {fruits}")

fruits.remove("banana")          # Remove by value
print(f"After remove: {fruits}")

popped = fruits.pop()            # Remove and return last item
print(f"Popped: {popped}, List: {fruits}")

# List indexing and slicing
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"First two: {fruits[0:2]}")

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original numbers: {numbers}")
numbers.sort()
print(f"Sorted: {numbers}")
numbers.reverse()
print(f"Reversed: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Count of 1: {numbers.count(1)}")

# List comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

even_numbers = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# ============================================================================
# 5. TUPLES (Ordered, Immutable)
# ============================================================================

# Creating tuples
coordinates = (10, 20)
person = ("John", 25, "Engineer")
single_item = (42,)  # Note the comma

print(f"Coordinates: {coordinates}")
print(f"Person: {person}")

# Tuple operations
print(f"First coordinate: {coordinates[0]}")
print(f"Name: {person[0]}, Age: {person[1]}")

# Tuple unpacking
x, y = coordinates
print(f"x: {x}, y: {y}")

name, age, profession = person
print(f"Unpacked - Name: {name}, Age: {age}, Profession: {profession}")

# ============================================================================
# 6. SETS (Unordered, Unique elements)
# ============================================================================

# Creating sets
colors = {"red", "green", "blue"}
numbers_set = {1, 2, 3, 4, 5}

print(f"Colors: {colors}")

# Set operations
colors.add("yellow")
print(f"After add: {colors}")

colors.remove("green")
print(f"After remove: {colors}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")
print(f"Symmetric difference: {set1 ^ set2}")

# ============================================================================
# 7. DICTIONARIES (Key-Value Pairs)
# ============================================================================

# Creating dictionaries
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics", "Chemistry"]
}

print(f"Student: {student}")

# Accessing values
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")
print(f"GPA: {student.get('gpa', 'Not found')}")  # Default value

# Modifying dictionaries
student["age"] = 21
student["gpa"] = 3.8
print(f"Updated student: {student}")

# Dictionary methods
print(f"Keys: {student.keys()}")
print(f"Values: {student.values()}")
print(f"Items: {student.items()}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dictionary: {squares_dict}")

# ============================================================================
# 8. OPERATORS
# ============================================================================

# Arithmetic operators
a, b = 10, 3
print(f"\n--- Arithmetic Operators ---")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a ** b}")

# Comparison operators
print(f"\n--- Comparison Operators ---")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

# Logical operators
print(f"\n--- Logical Operators ---")
x, y = True, False
print(f"{x} and {y}: {x and y}")
print(f"{x} or {y}: {x or y}")
print(f"not {x}: {not x}")

# ============================================================================
# 9. CONDITIONAL STATEMENTS
# ============================================================================

print(f"\n--- Conditional Statements ---")

# if-elif-else
score = 85

if score >= 90:
    grade = "A"
    print(f"Score: {score}, Grade: {grade}")
elif score >= 80:
    grade = "B"
    print(f"Score: {score}, Grade: {grade}")
elif score >= 70:
    grade = "C"
    print(f"Score: {score}, Grade: {grade}")
else:
    grade = "F"
    print(f"Score: {score}, Grade: {grade}")

# Ternary operator
age = 18
status = "Adult" if age >= 18 else "Minor"
print(f"Age: {age}, Status: {status}")

# ============================================================================
# 10. LOOPS
# ============================================================================

print(f"\n--- For Loops ---")

# For loop with range
for i in range(5):
    print(f"Number: {i}", end=" ")
print()

# For loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# For loop with enumerate
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# For loop with dictionary
person = {"name": "Bob", "age": 30, "city": "NYC"}
for key, value in person.items():
    print(f"{key}: {value}")

print(f"\n--- While Loops ---")

# While loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Break and continue
print(f"\n--- Break and Continue ---")
for i in range(10):
    if i == 3:
        continue  # Skip 3
    if i == 7:
        break     # Stop at 7
    print(f"i = {i}", end=" ")
print()

# ============================================================================
# 11. FUNCTIONS
# ============================================================================

print(f"\n--- Functions ---")

# Basic function
def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

print(greet("Alice"))

# Function with default parameters
def power(base, exponent=2):
    """Calculate power with default exponent of 2"""
    return base ** exponent

print(f"2^2 = {power(2)}")
print(f"2^3 = {power(2, 3)}")

# Function with multiple return values
def get_min_max(numbers):
    """Return minimum and maximum values"""
    return min(numbers), max(numbers)

numbers = [3, 7, 2, 9, 1, 5]
minimum, maximum = get_min_max(numbers)
print(f"Min: {minimum}, Max: {maximum}")

# Function with *args (variable positional arguments)
def sum_all(*args):
    """Sum all arguments"""
    return sum(args)

print(f"Sum: {sum_all(1, 2, 3, 4, 5)}")

# Function with **kwargs (variable keyword arguments)
def print_info(**kwargs):
    """Print all keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")

# Lambda functions (anonymous functions)
square = lambda x: x**2
print(f"Lambda square of 5: {square(5)}")

add = lambda x, y: x + y
print(f"Lambda add 3 + 4: {add(3, 4)}")

# Map, filter, reduce
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Mapped squares: {squared}")

even = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Filtered even: {even}")

from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(f"Reduced product: {product}")

# ============================================================================
# 12. CLASSES AND OBJECTS (OOP)
# ============================================================================

print(f"\n--- Object-Oriented Programming ---")

# Basic class
class Dog:
    """A simple Dog class"""
    
    # Class variable
    species = "Canis familiaris"
    
    # Constructor
    def __init__(self, name, age):
        """Initialize dog with name and age"""
        self.name = name  # Instance variable
        self.age = age
    
    # Instance method
    def bark(self):
        """Dog barks"""
        return f"{self.name} says Woof!"
    
    # String representation
    def __str__(self):
        return f"{self.name} is {self.age} years old"

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1)
print(dog2)
print(dog1.bark())
print(f"Species: {Dog.species}")

# Inheritance
class Puppy(Dog):
    """Puppy class inheriting from Dog"""
    
    def __init__(self, name, age, toy):
        super().__init__(name, age)
        self.toy = toy
    
    def play(self):
        return f"{self.name} plays with {self.toy}"

puppy = Puppy("Charlie", 1, "ball")
print(puppy)
print(puppy.bark())
print(puppy.play())

# ============================================================================
# 13. EXCEPTION HANDLING
# ============================================================================

print(f"\n--- Exception Handling ---")

# Try-except
try:
    result = 10 / 2
    print(f"Division result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Try-except-else-finally
try:
    number = int("123")
    print(f"Converted number: {number}")
except ValueError:
    print("Invalid number format!")
else:
    print("Conversion successful!")
finally:
    print("Cleanup code executed")

# Multiple exceptions
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except (IndexError, KeyError) as e:
    print(f"Error: {e}")

# Custom exception
class CustomError(Exception):
    """Custom exception class"""
    pass

def validate_age(age):
    if age < 0:
        raise CustomError("Age cannot be negative!")
    return age

try:
    validate_age(25)
    print("Age is valid")
except CustomError as e:
    print(f"Validation error: {e}")

# ============================================================================
# 14. FILE OPERATIONS
# ============================================================================

print(f"\n--- File Operations ---")

# Writing to a file
try:
    with open("sample.txt", "w") as file:
        file.write("Hello, Python!\n")
        file.write("This is a test file.\n")
        file.writelines(["Line 3\n", "Line 4\n"])
    print("File written successfully")
except IOError as e:
    print(f"File error: {e}")

# Reading from a file
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(f"File content:\n{content}")
except FileNotFoundError:
    print("File not found!")

# Reading line by line
try:
    with open("sample.txt", "r") as file:
        for line in file:
            print(f"Line: {line.strip()}")
except FileNotFoundError:
    print("File not found!")

# ============================================================================
# 15. LIST COMPREHENSIONS AND GENERATORS
# ============================================================================

print(f"\n--- List Comprehensions ---")

# List comprehension
squares = [x**2 for x in range(10)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested list comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
print(f"Matrix: {matrix}")

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

# Set comprehension
unique_squares = {x**2 for x in range(-5, 6)}
print(f"Unique squares: {unique_squares}")

# Generator expression
squares_gen = (x**2 for x in range(10))
print(f"Generator: {squares_gen}")
print(f"First three from generator: {[next(squares_gen) for _ in range(3)]}")

# ============================================================================
# 16. BUILT-IN FUNCTIONS
# ============================================================================

print(f"\n--- Built-in Functions ---")

numbers = [1, 2, 3, 4, 5]

print(f"len: {len(numbers)}")
print(f"sum: {sum(numbers)}")
print(f"min: {min(numbers)}")
print(f"max: {max(numbers)}")
print(f"sorted: {sorted([3, 1, 4, 1, 5])}")
print(f"reversed: {list(reversed(numbers))}")
print(f"abs: {abs(-42)}")
print(f"round: {round(3.14159, 2)}")
print(f"pow: {pow(2, 3)}")

# Type conversion
print(f"int('42'): {int('42')}")
print(f"float('3.14'): {float('3.14')}")
print(f"str(123): {str(123)}")
print(f"list('hello'): {list('hello')}")
print(f"tuple([1,2,3]): {tuple([1,2,3])}")
print(f"set([1,1,2,3]): {set([1,1,2,3])}")

# any and all
print(f"any([False, True, False]): {any([False, True, False])}")
print(f"all([True, True, True]): {all([True, True, True])}")

# zip
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = list(zip(names, ages))
print(f"zip: {combined}")

# enumerate
for index, value in enumerate(["a", "b", "c"]):
    print(f"enumerate: {index} -> {value}")

# ============================================================================
# 17. MODULES AND IMPORTS
# ============================================================================

print(f"\n--- Modules and Imports ---")

# Standard library imports
import math
import random
import datetime

print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Random number: {random.randint(1, 100)}")
print(f"Current date: {datetime.datetime.now()}")

# From import
from math import factorial, ceil
print(f"Factorial of 5: {factorial(5)}")
print(f"Ceil of 3.2: {ceil(3.2)}")

# ============================================================================
# 18. DECORATORS
# ============================================================================

print(f"\n--- Decorators ---")

# Simple decorator
def uppercase_decorator(func):
    """Decorator to convert result to uppercase"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
def greet_person(name):
    return f"hello, {name}"

print(greet_person("alice"))

# Decorator with arguments
def repeat(times):
    """Decorator to repeat function execution"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")
    return "Done"

say_hello()

# ============================================================================
# 19. WORKING WITH DATES AND TIMES
# ============================================================================

print(f"\n--- Date and Time ---")

from datetime import datetime, timedelta

now = datetime.now()
print(f"Current datetime: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Date arithmetic
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

last_week = now - timedelta(weeks=1)
print(f"Last week: {last_week.strftime('%Y-%m-%d')}")

# ============================================================================
# 20. USEFUL TIPS AND TRICKS
# ============================================================================

print(f"\n--- Tips and Tricks ---")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"Multiple assignment: x={x}, y={y}, z={z}")

# Swapping variables
a, b = 10, 20
a, b = b, a
print(f"Swapped: a={a}, b={b}")

# Unpacking
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
print(f"first={first}, middle={middle}, last={last}")

# String multiplication
print(f"'*' * 50: {'*' * 50}")

# Checking membership
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

# Get object type
print(f"Type of 42: {type(42)}")
print(f"Type of 'hello': {type('hello')}")

# Check if instance
print(f"isinstance(42, int): {isinstance(42, int)}")
print(f"isinstance('hello', str): {isinstance('hello', str)}")

# dir() - list attributes and methods
print(f"Methods of string: {[m for m in dir('') if not m.startswith('_')][:5]}...")

# ============================================================================

print("\n" + "="*80)
print("Python Basics Complete!")
print("="*80)
