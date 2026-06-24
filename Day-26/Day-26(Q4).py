score = 0

print("----- Quiz Application -----")

q1 = input("1. What is the capital of India? ")
if q1.lower() == "new delhi":
    score += 1

q2 = input("2. Which language is used for AI and Data Science? ")
if q2.lower() == "python":
    score += 1

q3 = input("3. How many continents are there? ")
if q3 == "7":
    score += 1

print("\nYour Score:", score, "/3")

if score == 3:
    print("Excellent!")
elif score == 2:
    print("Good Job!")
else:
    print("Keep Practicing!")
