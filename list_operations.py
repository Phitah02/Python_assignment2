'''PETER AKAMAU MWAURA - WEEK 2 ASSIGNMENT'''
# Python List Operations Assignment

# Step 1: Create an empty list called my_list
my_list = []

# Step 2: Append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After appending 10, 20, 30, 40:", my_list)

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)
print("After inserting 15 at second position:", my_list)

# Step 4: Extend my_list with [50, 60, 70]
my_list.extend([50, 60, 70])
print("After extending with [50, 60, 70]:", my_list)

# Step 5: Remove the last element
my_list.pop()
print("After removing last element:", my_list)

# Step 6: Sort my_list in ascending order
my_list.sort()
print("After sorting in ascending order:", my_list)

# Step 7: Find and print the index of value 30
index_of_30 = my_list.index(30)
print("Index of value 30:", index_of_30)
