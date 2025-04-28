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
