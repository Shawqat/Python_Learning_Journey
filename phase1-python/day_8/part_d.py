import csv
# Part D: CSV. Create students.csv with these rows: header name,score, then Sara,92, Omar,58, Lina,75, Yusuf,64. Read it with csv.DictReader, print the average score (expected 72.25), and print the names of students above the average (expected Sara, Lina).
# Don't forget the type conversion.import csv
with open("students.csv", "w") as f : 
	writer = csv.writer(f)
	writer.writerow(["name", "score"])
	writer.writerow(["Sara", 92])
	writer.writerow(["Omar", 58])
	writer.writerow(["Lina", 75])
	writer.writerow(["Yusuf", 64])

students_scores = 0
total_students = 0
with open("students.csv", "r") as f :
	for student in csv.DictReader(f):
		students_scores += int(student['score'])
		total_students += 1

average = students_scores / total_students
print(average)
with open("students.csv", "r") as f :
	for student in csv.DictReader(f):
		if float(student['score']) > average:
			print(student['name'])