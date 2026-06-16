arr = [1, 2, 2, 3, 4, 2, 5, 3]

max_freq = 0
max_element = arr[0]

for i in arr:
    count = 0
    for j in arr:
        if i == j:
            count += 1

    if count > max_freq:
        max_freq = count
        max_element = i

print("Maximum frequency element:", max_element)
print("Frequency:", max_freq)
