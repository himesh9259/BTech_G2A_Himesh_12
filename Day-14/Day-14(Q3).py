arr = [10, 25, 40, 15, 35]

largest = second = arr[0]

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest element is:", second)
