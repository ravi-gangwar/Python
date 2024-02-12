num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
num3 = int(input("Third Number: "))


if(num1 != 7 and num2 != 7 and num3 != 7):
    print(num1*num2*num3)
elif(num1 == 7 and num2 == 7 and num3 == 7):
    print("-1")
elif(num1 == 7 and num1 != 7 and num3 != 7):
    print(num2 * num3)
elif(num1 !=7 and num1 != 7 and num3 == 7):
    print("-1")
elif(num1 != 7 and num1 == 7 and num3 != 7):
    print(num3)




