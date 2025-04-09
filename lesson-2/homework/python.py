-------1
from datetime import date

today = date.today().year

a = input(str('write your name'))
b = int(input('What year were you born'))
c = today - b
print('Hello', a, 'you are', c, 'years old')

----3
txt = 'MsaatmiazD'.lower()

if "mazda" in txt:
    print("Found: mazda")

------4
txt = "I'am John. I am from London"
words = txt.split()
area = words[5]
print("Residence area:", area)

----5
a = str(input('Write your full name'))
print(a[::-1])

-----6
a = str(input('Write your name'))

vowels = ('aeiouAEIOU')
count = 0

for vow in txt:
    if vow in vowels:
        count += 1

print('in your name', count, 'vowels')

-------7
a = int(input('write a first random number'))
b = int(input('write a second random number'))
c = int(input('write a third random number'))
d = int(input('write a fourth random number'))
e = int(input('write a fifth random number'))

numbers = [a, b, c, d, e]
largest = max(numbers)
print(largest)

---8
a = str(input('write a word'))
if a == a[::-1]:
    print('your word is palindrome')
else:
    print("your word isn't palindrome ")

---9
email = input("Enter your email address: ")

if '@' in email:
    domain = email.split('@')[1]
    print("Domain:", domain)
else:
    print("Invalid email address. Please include '@'.")

----------10
