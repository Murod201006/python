# 1
Use python -m venv env to create a virtual environment.

Activate it and install necessary packages using pip install

# 2
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Cannot divide by zero"

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for char in s.lower() if char in 'aeiou')


# 3
# In circle.py
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

# in file_reader.py
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# in file_writer.py
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
