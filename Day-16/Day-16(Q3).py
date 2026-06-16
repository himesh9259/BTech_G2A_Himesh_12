arr = [1, 4, 5, 6, 3, 7]
target = 10

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Pair found:", arr[i], arr[j])
            
