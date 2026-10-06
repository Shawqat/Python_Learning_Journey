# import calc
# Part A: Predict first. Write answers before running,
#  and flag the line you're least sure about:

# import math
# from random import randint
# import json

# print(math.floor(3.9)) # output: 3
# print(math.ceil(3.1)) # output: 4
# print(type(json.dumps({"a": 1}))) # output: dumps convert from dict to json so it would be json or is it object this is the least sure line about it
# by Instructor: <class 'str'>
# print(json.loads('{"x": 5}')["x"]) # output: 5 
# print(10 <= randint(10, 20) <= 20) # output : True 

# Part B: Built-in toolkit. In toolkit.py:
# from random import randint, choice
# import datetime as dt
# import math
# Print a random number between 1 and 100
# def rand_number(start, end):
# 	return randint(start, end)


# Print today's date formatted like 2026-10-06
# def get_today_date():
# 	today_date = dt.datetime.now()
# 	return today_date.strftime("%Y-%m-%d")

# Print the square root of 144 rounded up with math.ceil
# def square_root(n):
# 	return math.ceil(math.sqrt(n))

# Pick a random item from ["red", "green", "blue"] and print it
# def rand_item(items):
# 	return choice(items)

# if __name__ == "__main__":
# 	print(rand_number(1, 100))
# 	print(get_today_date())
# 	print(square_root(12))
# 	print(rand_item(["red", "green", "blue"]))


# Part C: Your own module. Create calc.py with four functions: add, subtract, multiply, and divide (if the divisor is 0, return the string "Cannot divide by zero", don't crash and don't print). Then create main.py that imports calc and tests each function at least twice, including a divide-by-zero.
# I've created the file and include it using import statement
# there's many things i could add for this code but i did it like that 
# for the sake of simplesty.
# def add(num1, num2):
# 	return num1 + num2

# def subtract(num1, num2):
# 	return num1 - num2

# def multiply(num1, num2):
# 	return num1 * num2

# def divide(num1, num2):
# 	if num2 == 0:
# 		return "Cannot divide by zero"
# 	return num1 / num2

# Part D: The guard. Add test lines at the bottom of calc.py so they run when you execute python calc.py, but do not run when main.py imports it. Prove both by running each file and describing what you saw.

# ok I've added the following and run it 
# if __name__ == "__main__":
# 	print(add(5,7))
# 	print(divide(8,4))	

# if i didn't add the guard , it would be executed automatically when imported


# Part E: Bug hunt. Find and name every problem, then fix them in code. The goal is to print 4.0, a random die roll, and 6.0:

# import math
# from random import randint

# print(math.sqrt(16)
# print(random.randint(1, 6))
# print(sqrt(36))
# import Math


# the first error i notice missed parenthesis while using math.sqrt
# the second one it's using random.randint although we imported the randint right away i don't think we need to use like that. 
# the third one is using sqrt directly without refering to math module. 
# the fourth one is re import math module with capital letter which is not exist.
# so the code should be like that: 
# import math
# from random import randint

# print(math.sqrt(16))
# print(randint(1, 6))
# print(math.sqrt(36))

# Part F: JSON round trip. Given:

import json
# user = {"name": "Sara", "age": 28, "skills": ["python", "git"], "active": True}
# note : json converts None -> null, True -> true, False -> false, and tuples -> lists.
# Convert it to a JSON string, print it, convert it back to a dictionary, and print back["skills"][0]. Then answer in a comment: in the JSON string, how does True appear? (Compare it with the Python value.)


# first to json string
# to_json = json.dumps(user)
# print(to_json)

# then back to dict
# back = json.loads(to_json)
# print(back["skills"][0])
# we could make True appear using the following : back["active"]

# Part G (stretch): In collections there's a class called Counter.
#  Use help(Counter) or the docs to count the words in "the cat
#  and the hat and the bat" with one line,
#  and compare the result with your hand-built count_words from Day 6.

# what i did
# from collections import Counter as ct
# text = "the cat and the hat and the bat"
# text = text.split(" ")
# print(ct(text))
# same result but more elegant and easy 

