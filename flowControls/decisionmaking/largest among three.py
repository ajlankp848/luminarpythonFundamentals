num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
if(num1>num2)&(num1>num3):
    print("the  largest number is", num1)
elif(num2>num1)&(num2>num3):
    print("the  largest number is", num2)
elif(num3>num1)&(num3>num2):
    print("the largest number is", num3)
elif(num1==num2)&(num1==num3):
    print("the three numbers are equal")
else:
    pass