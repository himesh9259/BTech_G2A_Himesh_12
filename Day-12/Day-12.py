def palindrome(n):
    rev = 0
    temp = n

    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10

    if temp == rev:
        return True
    else:
        return False

num = int(input("Enter a number: "))

if palindrome(num):
    print("Palindrome")
else:
    print("Not Palindrome")
