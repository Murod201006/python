# 1
import numpy as np

lst = [12.23, 13.32, 100, 36.32]
array = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", array)
# 2
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)
# 3
null_vector = np.zeros(10)
print("Original null vector:", null_vector)
null_vector[6] = 11
print("After updating sixth value to 11:", null_vector)
# 4
array_12_38 = np.arange(12, 38)
print(array_12_38)
# 5
int_array = np.array([1, 2, 3, 4])
float_array = int_array.astype(float)
print("Original array:", int_array)
print("Array converted to float:", float_array)
# 6
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = celsius * 9 / 5 + 32
print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)
# 7
original_array = np.array([10, 20, 30])
new_array = np.append(original_array, [40, 50, 60, 70, 80, 90])
print("Original array:", original_array)
print("After append values to the end of the array:", new_array)
# 8
random_array = np.random.rand(10)
mean = np.mean(random_array)
median = np.median(random_array)
std_dev = np.std(random_array)

print("Random Array:", random_array)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
# 9
array_10x10 = np.random.rand(10, 10)
min_val = np.min(array_10x10)
max_val = np.max(array_10x10)

print("Random 10x10 Array:\n", array_10x10)
print("Minimum value:", min_val)
print("Maximum value:", max_val)
# 10
array_3x3x3 = np.random.rand(3, 3, 3)
print("3x3x3 Array with random values:\n", array_3x3x3)
