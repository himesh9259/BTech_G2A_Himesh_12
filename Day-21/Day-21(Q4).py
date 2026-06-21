# Convert lowercase to uppercase

s = input("Enter a string: ")

upper_str = ""

for ch in s:
    if 'a' <= ch <= 'z':
        upper_str += chr(ord(ch) - 32)
    else:
        upper_str += ch

print("Uppercase string =", upper_str)
