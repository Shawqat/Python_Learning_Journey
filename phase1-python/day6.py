# Part A: Predict first. Write your answers before running, and flag the line you're least sure about:

def double(n):
    return n * 2

def show(n):
    print(n * 2)

print(double(4)) # output : 8
a = show(4) # output: 8, but the return value is None
print(a) # output: None

def f():
    x = 5
    return x
    print("unreachable")

print(f()) # output: 5 only, cause whatever after return it won't be executed.

def g(a, b=10):
    return a + b

print(g(1)) # output: 11
print(g(1, 2)) # output: 3
print(g(b=5, a=1)) # output: 6

# Part B: Basic functions. Write and test each (call each at least twice with different inputs):

# is_even(n) returns True or False
# rectangle_area(width, height) returns the area
# shout(text) returns the text uppercased with "!" at the end (shout("hi") gives "HI!")

def is_even(n):
	if n % 2 == 0 :
		return True
	return False

print(is_even(2))
print(is_even(3))

def rectangle_area(width, height):
	return width * height

print(rectangle_area(4, 6)) 

def shout(text):
	return text.upper() + "!"
print(shout("hi"))

# Part C: Stats function. Write get_stats(numbers) that returns three values: the minimum, maximum, and average. Unpack the results and print them. Test with [4, 8, 15, 16, 23], which should give 4, 23, 13.2.

def get_stats(numbers):
	return min(numbers), max(numbers), sum(numbers) / len(numbers)

minimum, maximum, average = get_stats([4, 8, 15, 16, 23])
print(minimum, maximum, average)


# Part D: Refactor. Here's repeated code. Rewrite it using one function with parameters so there's no repetition:

# print("=== Welcome, Sara ===")
# print("Your balance is $120")
# print("=== Welcome, Omar ===")
# print("Your balance is $75")
# print("=== Welcome, Lina ===")
# print("Your balance is $300")

# Then call your function three times, or call it in a loop over a list of tuples.
customers = [("Sara", 120), ("Omar", 75), ("Lina", 300)]

def balance_info(name, balance):
	print(f"=== Welcome, {name} ===")
	print(f"Your balance is ${balance}")

for customer in customers:
	balance_info(customer[0], customer[1])

# ai version
# for name, balance in customers:
#     balance_info(name, balance)

# Part E: Bug hunt. Find and name every bug, then fix them in code.
#  The function should return the largest of three numbers;
#  the final output should be 9, then "Positive" for check(5) and "Negative" for check(-3).

def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

result = largest(3, 9, 4)
print(result)

def check(n):
    if n > 0:
        return "Positive"
    else:
        return "Negative"

label = check(5)
print(check(-3))
print(label)

# first the forgotten colon in function declaration and if condition
# second the indentation of return statement inside elif
# third we should return value not printing cause it save it as none value

# Part F: Password validator. Write is_strong_password(password) that returns True
#  only if the password is at least 8 characters and contains at least one digit
#  and contains at least one uppercase letter. Test with these and show the results:

# input		    expected
# "abc"	        False
# "abcdefgh"	False
# "abcdefg1"	False
# "Abcdefg1"	True

# this one i learned by reading
def is_strong_password(password):
    return (
        len(password) >= 8
        and any(ch.isdigit() for ch in password)
        and any(ch.isupper() for ch in password)
    )


print(is_strong_password("abc"))
print(is_strong_password("abcdefgh"))
print(is_strong_password("abcdefg1"))
print(is_strong_password("Abcdefg1"))


# Part G (stretch): Using your dictionary skills from Day 5,
#  write count_words(text) that returns a dictionary of word counts.
#  Test with "the cat and the hat" and expect {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}.

def count_words(text):
	word_counts = {}
	words = text.split(" ")
	for word in words:
		word_counts[word] = word_counts.get(word, 0) + 1
	return word_counts

print(count_words("the cat and the hat"))