n=int(input("Enter number:"))
orignal=n
sum =0
while n>0:
    sum+=(n%10)*(n%10)*(n%10)
    n//=10
if (orignal==sum):
    print("armstrong")
else:
    print("not armstrong")
