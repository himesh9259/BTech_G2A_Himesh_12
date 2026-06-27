# Marksheet Generation System

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

marks = []
subjects = ["English", "Maths", "Science", "Computer", "Hindi"]

for subject in subjects:
    mark = int(input(f"Enter marks in {subject}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / len(subjects)

# Grade Calculation
if percentage >= 90:
    grade = 'A+'
elif percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 50:
    grade = 'D'
else:
    grade = 'F'

print("\n========== MARKSHEET ==========")
print("Student Name :", name)
print("Roll Number  :", roll)

for i in range(len(subjects)):
    print(f"{subjects[i]} : {marks[i]}")

print("--------------------------------")
print("Total Marks :", total)
print("Percentage  :", round(percentage, 2), "%")
print("Grade       :", grade)

if percentage >= 40:
    print("Result      : PASS")
else:
    print("Result      : FAIL")
