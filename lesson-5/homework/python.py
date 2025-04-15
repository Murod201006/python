# 1
year = int(input('enter a year'))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('this year was leap year')
else:
    print("this year wasn't leap year")
# 2
n = int(input("Enter a number: "))

if n < 1 or n > 100:
    print("Input must be between 1 and 100")
else:
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")
# 3
# with if-else
def even_numbers_if_else(a, b):
    if a > b:
        a, b = b, a
    even_start = a if a % 2 == 0 else a + 1
    return list(range(even_start, b + 1, 2))
# without if-else
def even_numbers_no_if_else(a, b):
    even_start = a + (a % 2)  # Add 1 if a is odd
    return list(range(min(a, b) + (min(a, b) % 2), max(a, b) + 1, 2))
