string = input("Enter a string: ")
ch = input("Enter the character to find frequency: ")

count = 0

for i in string:
    if i == ch:
        count += 1

print("Frequency of", ch, "is", count)
