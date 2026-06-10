n = 5
i = 1

while i <= n:
    # Print spaces
    j = 1
    while j <= n - i:
        print(" ", end="")
        j += 1

    # Print ascending characters
    j = 0
    while j < i:
        print(chr(65 + j), end="")
        j += 1

    # Print descending characters
    j = i - 2
    while j >= 0:
        print(chr(65 + j), end="")
        j -= 1

    print()
    i += 1
