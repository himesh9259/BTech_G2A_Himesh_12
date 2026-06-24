def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False

    temp = str1 + str1
    return str2 in temp

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if is_rotation(str1, str2):
    print("Strings are rotations of each other")
else:
    print("Strings are not rotations of each other")
