n = int(input("Enter number of elements: "))

arr = []
total = 0

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
    total += num

average = total / n

print("Array:", arr)
print("Sum =", total)
print("Average =", average)
