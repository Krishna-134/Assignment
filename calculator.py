print("SIMPLE CALCULATOR")
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
n=int(input("ENTER THE CHOICE 1.add:\n 2.substraction:\n 3.multiply:\n 4.division:\n"))
if(n==1):
    c=a+b
    print(c)
elif(n==2):
    c=a-b
    print(c)
elif(n==3):
    c=a*b
    print(c)
elif(n==4):
    c=a/b
    print(c) 
else:
    print("invalid choice")

