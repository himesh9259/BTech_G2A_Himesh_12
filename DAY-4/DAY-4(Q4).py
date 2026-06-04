start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

print("Armstrong numbers are:")

for num in range(start, end + 1):
    order = len(str(num))
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** order
        temp //= 10

    if num == total:
        print(num)
