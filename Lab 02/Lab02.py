# Activity 01
# Use loops to accept 5 values from user and store them in a list. Display all the values
# (objects) of the list.

# # Create an empty list
# list = []

# # Accept 5 values from user
# for i in range(5):
#     list.append(input("Enter a value: "))

# # Display all the values (objects) of the list
# print("The List is")
# print(list)

# Activity 02
# # Create an empty list
# list = []

# # Accept 5 values from user
# for i in range(5):
#     val = int((input("Enter a value: ")))
#     list.append(val)

# # Display all the values (objects) of the list
# sum = 0
# for val in list:
#     sum = sum + val

# print(sum)

# Activity 03
# # Create an empty list
# list = []

# # Accept 5 values from user
# for i in range(5):
#     list.append(input("Enter a value: "))

# # Display all the values (objects) of the list
# list.sort()
# print(list)

# Activity 04
# Create an empty list
# list1 = []

# # Accept 5 values from user
# for i in range(5):
#     list1.append(input("Enter a value: "))

# # Display all the values (objects) of the list

# # Create an empty list
# list2 = []

# # Accept 5 values from user
# for i in range(5):
#     list2.append(input("Enter a value: "))

# # Display all the values (objects) of the list

# list3 = list1 + list2
# print(list3)

# Activity 05
# Create an empty list
# list = []

# # Accept 5 values from user
# for i in range(5):
#     list.append(input("Enter a value: "))

# # Display all the values (objects) of the list
# print("The List is")
# print(list)

# n = int(input("Enter a number: "))
# found = n in list

# if found == True:
#     print("Found")
# else:
#     print("Not Found")

# Activity 06
# def say_hello(name):
#     print("Hello", name)


# say_hello("Amit")
# say_hello("Rohan")
# say_hello("Shubham")
# say_hello("Saurabh")


# Activity 07
# def check_palindrome(str):
#     if str == str[::-1]:
#         return True
#     else:
#         return False


# print(check_palindrome("madaam"))

# Activity 08
# Imagine two matrices given in the form of 2D lists as under;
# a = [[1, 0, 0], [0, 1, 0], [0, 0, 1] ]
# b = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
# Write a python code that finds another matrix/2D list that is a product of and b, i.e.,
# C=a*b

# a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# c = []

# c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for i in range(len(a)):
#     row = []
#     for j in range(len(b[0])):
#         for k in range(len(b)):
#             c[i][j] += a[i][k] * b[k][j]

# print(c)

# Activity 09

# Activity 10
