# Dictionary Exercises
# 1
sample_dict = {'a': 3, 'b': 1, 'c': 2}

sorted_asc = dict(sorted(sample_dict.items(), key=lambda item: item[1]))
print("Sorted Ascending:", sorted_asc)

sorted_desc = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))
print("Sorted Descending:", sorted_desc)
# 2
my_dict = {0: 10, 1: 20}
my_dict[2] = 30
print("After Adding a Key:", my_dict)
# 3
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

concatenated_dict = {**dic1, **dic2, **dic3}
print("Concatenated Dictionary:", concatenated_dict)
# 4
n = 5
squares_dict = {x: x*x for x in range(1, n+1)}
print(f"Squares Dictionary (1 to {n}):", squares_dict)
# 5
squares_1_to_15 = {x: x**2 for x in range(1, 16)}
print("Squares Dictionary (1 to 15):", squares_1_to_15)


# Set Exercises
# 1
my_set = {1, 2, 3, 4, 5}
print("Created Set:", my_set)
# 2
print("Iterating over the set:")
for item in my_set:
    print(item)
# 3
my_set.add(6)
my_set.update([7, 8])
print("Set after adding members:", my_set) 
# 4
my_set.discard(2)
my_set.remove(3)
print("Set after removing items:", my_set)
# 5
item_to_remove = 10
if item_to_remove in my_set:
    my_set.remove(item_to_remove)
    print(f"Item {item_to_remove} removed.")
else:
    print(f"Item {item_to_remove} not found in set.")
