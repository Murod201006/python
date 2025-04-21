# 1
def is_prime(n):
    if n <= 1:
        return False  # 1 yoki kichik sonlar tub emas
    for i in range(2, int(n**0.5) + 1):  # n ga teng yoki kichik bo'lgan sonlar orasida tekshirish
        if n % i == 0:
            return False  # Agar bo'linsa, tub emas
    return True  # Agar hech qanday bo'linuvchi topilmasa, tub son

# Misollar:
print(is_prime(4))  # Natija: False
print(is_prime(7))  # Natija: True
# 2
def digit_sum(k):
    # k ni stringga o'zgartirib, har bir raqamni yig'ish
    return sum(int(digit) for digit in str(k))

# Misollar:
print(digit_sum(24))   # Natija: 6
print(digit_sum(502))  # Natija: 7
# 3
def powers_of_two(n):
    k = 1
    result = []
    while 2**k <= n:
        result.append(2**k)
        k += 1
    return result

# Misol:
print(powers_of_two(10))  # Natija: [2, 4, 8]
