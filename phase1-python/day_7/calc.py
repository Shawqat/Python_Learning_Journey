# Part C: Your own module. Create calc.py with four functions: add, subtract, multiply, and divide (if the divisor is 0, return the string "Cannot divide by zero", don't crash and don't print). Then create main.py that imports calc and tests each function at least twice, including a divide-by-zero.
# I've created the file and include it using import statement
# there's many things i could add for this code but i did it like that 
# for the sake of simplesty.
def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	if num2 == 0:
		return "Cannot divide by zero"
	return num1 / num2