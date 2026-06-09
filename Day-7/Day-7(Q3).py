def sum_digit(n):
    if(n==0):
        return 0
    return n%10 + sum_digit(n//10)
num = int(input("enter number"))
print(sum_digit(num))
