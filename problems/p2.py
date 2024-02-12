num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))
num3 = int(input("Third Number: "))

if(((num1 + num2) > num3) and ((num2 + num3 ) > num1 ) and (num3 + num1) > num2):
    print("Yes it can form a Trinagle")
else:
    print("It can't")
