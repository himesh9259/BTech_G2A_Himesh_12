string = input("Enter a string: ")

new_string = ""

for ch in string:
    if ch != " ":
        new_string += ch

print("String without spaces:", new_string)
