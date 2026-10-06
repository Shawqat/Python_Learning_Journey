# Part A: Predict first (write answers before running):

# for i in range(4):
#     print(i)
# # 0 1 2 3

# for i in range(2, 8, 2):
#     print(i)
# # 2 4 6

# x = 10
# while x > 7:
#     x -= 1
# print(x)
# 7

# total = 0
# for n in range(1, 4):
#     total += n * 2
# print(total)
# # 12

# Part B: Countdown. Ask for a positive integer and count down to 1 with a while loop, then print "Go!".

# number = int(input("Enter a positive integer: "))
# number = int(input("Enter a positive integer: "))
# while number > 0:
#     print(number)
#     number -= 1
# print("Go!")

# Part C: Sum and average. 
# Use a for loop with range to ask the user for 5 numbers, 
# one at a time. Print the sum and the average with 2 decimals.

# total = 0
# for i in range(5):
#     num = float(input(f"Enter number {i + 1}: "))
#     total += num
# print(f"sum is = {total:.2f}, average is = {total / 5:.2f}")

# Part D: Bug hunt. Find and fix all the problems in this code.
#  This time I won't tell you how many there are.
#  It should print the even numbers from 1 to 10.

# n = 1
# while n <= 10
#     if n % 2 == 0:
#         print(n)
#     n += 1

# Part E: Password retry. The correct password is "python123". 
# Give the user a maximum of 3 attempts and print "Access granted" if they get it right, 
# or "Account locked" after 3 failures. Print how many attempts remain after each wrong guess. 
# correct_password = "python123"
# attempts = 3
# while attempts > 0:
#     password = input("Enter the password: ")
#     if password == correct_password:
#         print("Access granted")
#         break
#     else:
#         attempts -= 1
#         if attempts > 0:
#             print(f"Incorrect password. You have {attempts} attempts remaining.")
#         else:
#             print("Account locked.")

# Part F (stretch): Print this pattern using nested loops, or a single loop and string multiplication ("*" * 3 gives ***):

# *
# **
# ***
# ****
# *****

for i in range(1,7):
    print("*" * i)