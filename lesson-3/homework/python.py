# 1
fruits = ["apple", "banana", "grapes", "orange", "mango"]

print(fruits[2])

# 2
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2

print(combined_list)

# 3
numbers = [10, 11, 12, 13, 14, 15, 16]

first = numbers[0]
middle = numbers[len(numbers) // 2]
last = numbers[-1]

a = [first, middle, last]

print(a)

# 4
fm = ["Harry Potter", "Superman", "Prison Break", "Spider-man", "Thor"]

movies_tuple = tuple(fm)

print(movies_tuple)

# 5
cities = ["London", "New York", "Tokyo", "Paris", "Moscow", "Tashkent"]

if "Paris" in cities:
    print("Paris is in the list.")
else:
    print("Paris is not in the list.")

# 6
numbers = [1, 2, 3]
duplicated = numbers * 2
print(duplicated)

# 7
numbers = [10, 20, 30, 40, 50]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)

# 8
t = tuple(range(1, 11))
print(t[3:7])

# 9
colors = ["blue", "red", "blue", "green", "blue"]
print(colors.count("blue"))

# 10
animals = ("cat", "dog", "lion", "tiger")
print(animals.index("lion"))

# 11
a = (1, 2, 3)
b = (4, 5, 6)
print(a + b)

# 12
lst = [1, 2, 3, 4]
tpl = (5, 6, 7)
print(len(lst), len(tpl))

# 13
tpl = (10, 20, 30, 40, 50)
print(list(tpl))

# 14
number = (3, 8, 1, 6, 9)
print(max(number), min(number))

# 15
words = ("hello", "world", "python", "sql")
print(words[::-1])
