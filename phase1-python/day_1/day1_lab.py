# Part A: Predict first, then run. Before running, write down what each line prints, then check yourself:
print(10 // 3) 
print(10 % 3)
print("5" + "5")
print(int("5") + int("5"))
print(type(3.0))
print(type("3.0"))

# Part B: Build a program that:
# Asks for the user's name and the year they were born (input)
# Calculates their approximate age (use 2026)
# Prints: Hi Sara, you are about 28 years old.
user_name = input("What is your name? ")
user_age  = int(input("What year were you born? "))
approximate_age = 2026 - user_age
print(f"Hi {user_name}, you are about {approximate_age} years old.")

# Part C: Bug hunt. This code crashes. Find out why and fix it:
# age = input("Age? ")
# print(age + 5)  # we can't add string to integer, we should convert it first.

# Part D (stretch): Ask for a price and a quantity, then print the total with exactly 2 decimals.
price    = float(input("Enter the price: "))
quantity = int(input("Enter the quantity: "))

total = price * quantity
print(f"Total: ${total:.2f}")