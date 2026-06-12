# Function to find factorial of a number

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

# Input from user
num = int(input("Enter a number: "))

# Function call
result = factorial(num)

print("Factorial =", result)
