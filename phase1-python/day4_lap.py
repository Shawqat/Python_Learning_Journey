# Part A: Predict first. Write your answers before running, and use a trace if unsure:

nums = [10, 20, 30, 40, 50]
print(nums[-2]) # 40
print(nums[1:4]) # [20, 30, 40]
print(nums[::2]) # [10, 30, 50]

a = [1, 2, 3]
b = a # [1, 2, 3]
b.append(9) # [1, 2, 3, 9]
print(a) # [1, 2, 3]

t = (1, 2, 3)
print(t[1]) # 2

x = [3, 1, 2]
x = x.sort() # [1, 2, 3]
print(x) # [1, 2, 3]

# Part B: Shopping list. Start with cart = ["milk", "eggs"]. Then, in code: add "bread" to the end,
#  insert "coffee" at the front, remove "eggs", and print the cart and how many items it has.
#  Expected final cart: ['coffee', 'milk', 'bread'], 3 items.
cart = ["milk", "eggs"]
cart.append("bread")
cart.insert(0, "coffee")
cart.remove("eggs")
print(f"{cart}, {len(cart)} items")

# Part C: Stats. Ask the user for 5 numbers, store them in a list, and print the list, the sum,
#  the minimum, the maximum, and the average (2 decimals). Last time the lesson was verification,
#  so test with 4 8 15 16 23 first. The sum should be 66 and the average 13.20.
nums = []
for num in range(5):
    num = float(input(f"Enter number {num + 1}: "))
    nums.append(num)
print(f"sum = {sum(nums)}, min = {min(nums)}, max = {max(nums)}, average = {sum(nums)/len(nums):.2f}")

# Part D: Filtering. Given words = ["apple", "kiwi", "banana", "fig", "cherry"],
# build a new list containing only the words with 5 or more letters. 
# Do it once with a normal loop and once with a list comprehension. 
# Both should print ['apple', 'banana', 'cherry'].
words = ["apple", "kiwi", "banana", "fig", "cherry"]
# normal loop
new_list_normal = []
for item in words:
    if len(item) >= 5:
        new_list_normal.append(item)

new_list = [item for item in words if len(item) >= 5] # list comprehension
print(f"Normal loop: {new_list_normal}")
print(f"List comprehension: {new_list}")

# Part E: Bug hunt. There are several problems here. Find them all.
#  The code should print each fruit with its position starting from 1.

fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i+1}. {fruits[i]}")

# ai version :
# for position, fruit in enumerate(fruits, start=1):
#     print(f"{position}. {fruit}")

# print(fruits[3]) # This line will cause an IndexError because the index is out of range.
# Expected output:

# 1. apple
# 2. banana
# 3. cherry

# Part F (stretch): Remove duplicates, keeping the order. Given data = [1, 2, 2, 3, 1, 4, 3],
#  create a new list with each value once,
#  in first-seen order: [1, 2, 3, 4]. Use a loop and an if ... not in ... check.
data = [1, 2, 2, 3, 1, 4, 3]
unique_data = []
for num in data:
    if num not in unique_data:
        unique_data.append(num)
print(unique_data)