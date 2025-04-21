# 1
def insert_underscore(txt):
    result = []
    i = 0
    count = 0
    vowels = 'aeiouAEIOU'

    while i < len(txt):
        result.append(txt[i])
        count += 1
        if count == 3:
            if (i + 1 < len(txt)) and (txt[i] in vowels or txt[i + 1] == '_'):
                pass
            else:
                if i + 1 < len(txt):
                    result.append('_')
                    count = 0
                else:
                    break
        i += 1

    return ''.join(result)

print(insert_underscore("hello"))
print(insert_underscore("assalom"))
print(insert_underscore("abcabcabcdeabcdefabcdefg")) 


# 2
n = int(input())

for i in range(n):
    print(i ** 2)

# 3
# first exer
i = 1
while i <= 10:
    print(i)
    i += 1
# second exer
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print() 
# third exer
num = int(input("Enter number: "))
total = 0
i = 1
while i <= num:
    total += i
    i += 1
print("Sum is:", total)

# 4
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num * i)

# 5
numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if 75 <= num <= 150:
        print(num)
  
# 6
num = int(input("Enter a number: "))
count = 0

while num > 0:
    num = num // 10
    count += 1

print("Total digits:", count)
      
# 7
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# 8
list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])
  
# 9
for i in range(-10, 0):
    print(i)
  
# 10
for i in range(5):
    print(i)
else:
    print("Done!")

# 11
start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
# 12
n_terms = 10
a, b = 0, 1

print("Fibonacci sequence:")

for _ in range(n_terms):
    print(a, end=' ')
    a, b = b, a + b
# 13
num = int(input("Enter a number: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")


# 4
def uncommon_elements(list1, list2):
    result = [elem for elem in list1 if elem not in list2] + [elem for elem in list2 if elem not in list1]
    return result

list1 = [1, 1, 2]
list2 = [2, 3, 4]
print(uncommon_elements(list1, list2))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(uncommon_elements(list1, list2))

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
print(uncommon_elements(list1, list2))
