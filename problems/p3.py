x = int(input("How many number of Coin of 5 rupees: "))
y = int(input("How many number of Coin of 1 rupees: "))


amount = int(input("Amount of Purchased: "))

if((x*5 + y) != amount):
    print("-1")
else:
    oneRupees = amount%5

    fiveRupees = amount/5

    print("One rupee coins are: ", oneRupees,", " "5 ruppes coins are: ", fiveRupees)


