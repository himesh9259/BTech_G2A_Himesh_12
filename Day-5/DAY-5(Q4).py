num = int(input("Enter a number: "))

largest_factor = 1
i = 2

while i <= num:
    if num % i == 0:
        largest_factor = i
        num //= i
    else:
        i += 1

print("Largest Prime Factor =", largest_factor)
