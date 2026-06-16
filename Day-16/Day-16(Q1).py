arr = [1, 2, 3, 5]

n = len(arr) + 1

total = n * (n + 1) // 2
arr_sum = sum(arr)

missing = total - arr_sum

print("Missing number is:", missing)
