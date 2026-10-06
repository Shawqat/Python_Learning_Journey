# Part A: Predict first. Write your answers before running:

d = {"a": 1, "b": 2}
print(d["a"]) # 1
print(d.get("z")) # error
print(d.get("z", 0)) # 0 as a fallback value
print("b" in d) # true
print(2 in d) # false cause it looks in keys not values
print(len({1, 2, 2, 3, 3, 3})) # 3 cause it removes duplicate values
print(type({})) # dictionary
print({1, 2, 3} & {2, 3, 4}) # {2,3} cause it's intersection

# Part B: Contact card. Create a dictionary for yourself with name, email, and skills (a list of 3 skills). Then, in code: add a city key, change the email, append a 4th skill, and print every key and value with a loop using .items().

contact_card = {
"name": "Ahmed",
"email": "Ahmed@gmail.com",
"skills": ["html","css","js","Python"]
}

contact_card["city"] = "Asyut"
contact_card["email"] = "A@gmail.com"
contact_card["skills"].append("Git")
for key, value in contact_card.items():
	print(f"{key} : {value}")


text = "the cat and the hat and the bat"
words = text.split()
counts = {}
# your loop here, using counts.get(word, 0) + 1
# Print each word and its count on its own line.
for word in words:
	counts[word] = counts.get(word, 0) + 1

for word, count in counts.items():
	print(f"{word}: {count}")

# Part D: List of dictionaries. Given:

students = [
    {"name": "Sara", "score": 92},
    {"name": "Omar", "score": 58},
    {"name": "Lina", "score": 75},
    {"name": "Yusuf", "score": 64},
]

# Print the names of students who passed (score ≥ 60). Print the average score with 2 decimals (expected 72.25). Print the name of the student with the highest score (Sara).

print([student["name"] for student in students if student["score"] >= 60])
students_scores = [student["score"] for student in students]
students_numbers = len(students)
students_total_score = sum(students_scores)
print(f"avg score : {students_total_score/students_numbers:.2f}")

highest_student_score = 0
highest_student_name = ""
for student in students :
	if student["score"] > highest_student_score:
		highest_student_score = student["score"]
		highest_student_name = student["name"]

print(f"Highest Student: {highest_student_name} with score : {highest_student_score}")

# Part E: Bug hunt. Find and name every problem. This time please list each bug in your own words before fixing it. The code should print each product's price and then the total.

cart = {"pen": 2.50, "book": 12.00, "bag": 30.00}

total = 0
for item in cart:
    print(f"{item}: ${cart[item]}")
    total += cart[item]
print(f"Total: {total}")
print(cart.get("lamp", "lamp is not in the cart"))

# first we forgot colon in for loop, 
# second we need to use brackets with cart in print 
# the last print well throw an error cause the key is not exist we could fix it using get method.

# Part F: Sets. Two classes: class_a = ["Sara", "Omar", "Lina", "Omar"] and
# class_b = ["Lina", "Yusuf", "Sara", "Yusuf"]. Using sets, print (1) 
# every unique student across both classes, (2) students in both classes, 
# (3) students in class_a only. Expected: {'Sara', 'Omar', 'Lina', 'Yusuf'}, {'Sara', 'Lina'}, {'Omar'}
# (set order may differ).


class_a = {"Sara", "Omar", "Lina", "Omar"}
class_b = {"Lina", "Yusuf", "Sara", "Yusuf"}
# 1 unique i could combine them after that
print(class_a | class_b)


# 2 in both i could write one line
print(class_a & class_b)
print(class_b & class_a) 

# 3 students only in class a
print(class_a - class_b)


# Part G (stretch): Walk this nested data and print "Sara lives in Cairo" using indexing only, no loops:

company = {"team": [{"name": "Sara", "address": {"city": "Cairo"}}]}

print(f"{company["team"][0]["name"]} lives in {company["team"][0]["address"]["city"]}")