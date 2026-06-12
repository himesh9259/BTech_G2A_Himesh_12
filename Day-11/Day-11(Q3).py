# Function to check whether a number is prime

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

# Input from user
num = int(input("Enter a number: "))

# Function call
if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is not a Prime Number")
