# Count set bits manually

num = int(input("Enter a number: "))

count = 0

while num > 0:
    count += num % 2
    num //= 2

print("Number of set bits:", count)
