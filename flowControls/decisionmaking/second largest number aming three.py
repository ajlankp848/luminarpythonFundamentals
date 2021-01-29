num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print("the second largest number is", num2)
        print(num1,num2,num3)
    else:
        print("the second lagest number is", num3)
        print(num1,num3,num2)
elif(num2>num3)&(num2>num1):
    if(num1>num3):
        print("the second largest number is", num1)
        print(num2,num1,num3)
    else:
        print("the second largest number is", num3)
        print(num2,num3,num1)

elif(num3>num2)&(num3>num1):
    if(num2>num1):
        print("the second largest number is", num2)
        print(num3,num2,num1)
    else:
        print("the second largest number is",num1)
        print(num3,num1,num2)
else:
    pass
