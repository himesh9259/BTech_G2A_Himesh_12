n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Array elements are:")
for i in arr:
    print(i, end=" ")
