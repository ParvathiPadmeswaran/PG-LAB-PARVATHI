def cal(a,b):
    sum=a+b
    diff=a-b
    prod=a*b
    quo=a/b
    return sum,diff,prod,quo
a=int(input("enter first number : "))
b=int(input("enter second number : "))
s,d,p,q=cal(a,b)
print("sum=",s,"\ndifference=",d,"\nproduct=",p,"\nqotient=",q)
