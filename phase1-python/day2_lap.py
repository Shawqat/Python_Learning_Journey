# Part A: Predict first (write your answers before running):

# print(5 == "5") #false
# print(10 > 3 and 4 > 9) #false
# print(not (2 > 1)) #false
# print("a" in "banana") #true
# print(bool("")) #false
# print(bool("False")) #true

# Part B: Grade calculator. Ask for a score (0-100),
#  convert it to a number, and print the grade: 90+ is A, 80+ is B, 70+ is C, 60+ is D,
#  otherwise F. Show only the one matching grade.

score = int(input("Enter your score (0-100): "))

if score >= 90:
    print("Your grade is A.")
elif score >= 80:
    print("Your grade is B.")
elif score >= 70:
    print("Your grade is C.")
elif score >= 60:
    print("Your grade is D.")
else:
    print("Your grade is F.")

# Part C: Bug hunt. There are two bugs in this code. Find both and explain each:

# the error is in indentation and the comparison operator, colon missing, type error.
# temperature = input("Temperature: ")
# if temperature = 30:
# print("Hot")
# else
#     print("Not hot")

# Part D: Login checker. Ask for a username and password. Use these rules:

# If either field is empty, print "Fields cannot be empty"
# Else if the username is "admin" and the password is "1234", print "Welcome"
# Else print "Invalid credentials"
username = input("Enter your username: ")
password = input("Enter your password: ")

if not username or not password:
    print("Fields cannot be empty")
elif username == "admin" and password == "1234":
    print("Welcome")
else:
    print("Invalid credentials")

# Part E (stretch): Ask for a year and print whether it is a leap year.
#  A leap year is divisible by 4, except years divisible by 100, unless also divisible by 400.
#  Test it with 2000, 1900, 2024, and 2026.

year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")