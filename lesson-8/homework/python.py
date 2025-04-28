# exeption

# 1
try:
    num = int(input("Enter a number: "))
    result = num / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# 2
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: That was not a valid integer!")

# 3
try:
    with open('somefile.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")

# 4
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")
    if not (a.replace('.', '', 1).isdigit() and b.replace('.', '', 1).isdigit()):
        raise TypeError("Inputs must be numbers.")
    result = float(a) + float(b)
    print("Sum:", result)
except TypeError as e:
    print("Error:", e)

# 5
try:
    with open('protected_file.txt', 'w') as file:
        file.write("Trying to write to a protected file.")
except PermissionError:
    print("Error: You do not have permission to write to this file!")

# 6
my_list = [1, 2, 3]
try:
    index = int(input("Enter an index: "))
    print(my_list[index])
except IndexError:
    print("Error: List index out of range!")

# 7
try:
    number = input("Enter a number (Press Ctrl+C to cancel): ")
    print("You entered:", number)
except KeyboardInterrupt:
    print("\nInput cancelled by the user.")

# 8
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ArithmeticError as e:
    print("Arithmetic Error:", e)

# 9
try:
    with open('some_text.txt', 'r', encoding='ascii') as file:
        content = file.read()
        print(content)
except UnicodeDecodeError:
    print("Error: Cannot decode file contents due to encoding issue!")

# 10
my_list = [1, 2, 3]
try:
    my_list.appendd(4)  # Typo: should be append()
except AttributeError:
    print("Error: Attribute does not exist!")


# File input
# 1
with open('example.txt', 'r') as file:
    data = file.read()
    print(data)

# 2
def read_first_n_lines(filename, n):
    with open(filename, 'r') as file:
        for _ in range(n):
            print(file.readline(), end='')

read_first_n_lines('example.txt', 3)

# 3
with open('example.txt', 'a') as file:
    file.write("\nNew appended line.")

with open('example.txt', 'r') as file:
    print(file.read())

# 4
from collections import deque

def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = deque(file, maxlen=n)
    for line in lines:
        print(line, end='')

read_last_n_lines('example.txt', 3)

# 5
with open('example.txt', 'r') as file:
    lines = file.readlines()
print(lines)

# 6
with open('example.txt', 'r') as file:
    data = ''
    for line in file:
        data += line
print(data)

# 7
with open('example.txt', 'r') as file:
    array = [line.strip() for line in file]
print(array)

# 8
def find_longest_words(filename):
    with open(filename, 'r') as file:
        words = file.read().split()
    longest = max(words, key=len)
    print(longest)

find_longest_words('example.txt')

# 9
with open('example.txt', 'r') as file:
    line_count = sum(1 for line in file)
print("Number of lines:", line_count)

# 10
from collections import Counter

with open('example.txt', 'r') as file:
    words = file.read().replace(',', ' ').split()
    word_counts = Counter(words)

print(word_counts)

# 11
import os

size = os.path.getsize('example.txt')
print(f"File size: {size} bytes")

# 12
lines = ['First line', 'Second line', 'Third line']

with open('output.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')

# 13
with open('example.txt', 'r') as src, open('copy.txt', 'w') as dest:
    dest.write(src.read())

# 14
with open('file1.txt', 'r') as f1, open('file2.txt', 'r') as f2:
    for line1, line2 in zip(f1, f2):
        print(line1.strip() + " " + line2.strip())

# 15
import random

with open('example.txt', 'r') as file:
    lines = file.readlines()
    print(random.choice(lines).strip())

# 16
file = open('example.txt', 'r')
print(file.closed)  # False
file.close()
print(file.closed)  # True

# 17
with open('example.txt', 'r') as file:
    content = file.read().replace('\n', ' ')
print(content)

# 18
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.replace(',', ' ').split()
    return len(words)

print(count_words('example.txt'))

# 19
files = ['file1.txt', 'file2.txt']
chars = []

for filename in files:
    with open(filename, 'r') as file:
        chars.extend(list(file.read()))

print(chars)

# 20
import string

for letter in string.ascii_uppercase:
    with open(f'{letter}.txt', 'w') as file:
        file.write(f"This is file {letter}.txt")

# 21
def create_alphabet_file(letters_per_line):
    import string
    letters = string.ascii_uppercase
    with open('alphabet.txt', 'w') as file:
        for i in range(0, len(letters), letters_per_line):
            file.write(''.join(letters[i:i+letters_per_line]) + '\n')

create_alphabet_file(5)
