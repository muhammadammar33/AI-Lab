# Activity 9 and 10
# n = int(input("Enter interger: "))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # Activity 11
# # sum of numbers from 1 to 10 using while
# n = 1
# sum = 0
# while n <= 10:
#     sum += n
#     n += 1
# print(sum)

# # Activity 12
# sum = 0
# i = 0
# while i <= 4:
#     s = int(input("Enter Number: "))
#     sum = sum + s
#     i = i+1
# print(sum)

# Activity 13
# n = int(input("Enter Number: "))
# sum = 0
# while n != 0:
#     sum = sum + n
#     n = int(input("Enter Number: "))
# print(sum)

# Activity 14
# isPrime = True
# i = 2
# n = int(input("Enter number: "))
# while i < n:
#     remainder = n % i
#     if remainder == 0:
#         isPrime = False
#         break
#     else:
#         i = i+1

# if isPrime:
#     print("Prime")
# else:
#     print("Not Prime")

# Home Activity
# Activity 01
# Write a Python code to accept marks of a student from 1-100 and display the grade
# according to the following formula.
# Grade F if marks are less than 50 Grade E if marks are between 50 to 60 Grade D if marks
# are between 61 to 70 Grade C if marks are between 71 to 80 Grade B if marks are
# between 81 to 90
# Grade A if marks are between 91 to 100

# marks = int(input("Enter marks: "))

# if marks < 50:
#     print("Grade F")

# if marks >= 50 and marks < 60:
#     print("Grade E")

# if marks >= 60 and marks < 70:
#     print("Grade D")

# if marks >= 70 and marks < 80:
#     print("Grade C")

# if marks >= 80 and marks < 90:
#     print("Grade B")

# if marks >= 90 and marks <= 100:
#     print("Grade A")

# Activity 02
# Write a program that takes a number from user and calculate the factorial of that
# number.
# n = int(input("Enter Number: "))

# fact = 1

# for i in range(1, n+1):
#     fact = fact * i

# print(fact)

# Assignment Activities
# Fibonacci series is that when you add the previous two numbers the next number is formed.
# You have to start from 0 and 1.
# So the series becomes
# Steps: You have to take an input number that shows how many terms to be displayed.
# Then use loops for displaying the Fibonacci series up to that term e.g. input no is =6 the
# output should be
# 0 1 1 2 3 5

# n = int(input("Enter Number: "))

# a = 0

# b = 1

# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c
