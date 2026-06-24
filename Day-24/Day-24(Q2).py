def compress_string(s):
    compressed = ""
    count = 1

    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            compressed += s[i] + str(count)
            count = 1

    return compressed

string = input("Enter a string: ")
print("Compressed string:", compress_string(string))
