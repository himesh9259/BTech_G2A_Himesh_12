# Find x^n without using pow()

x = int(input("Enter the base (x): "))
n = int(input("Enter the exponent (n): "))

result = 1

for i in range(n):
    result *= x

print(f"{x}^{n} =", result)
