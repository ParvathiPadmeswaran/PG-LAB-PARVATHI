a=int(input("enter number \n"))
def fact(fact=1):
    for i in range(1,a+1):
        fact=fact*i
        i=i+1
    print("fac",fact)
fact()
