import random 

jackpot = random.randint(1,100)

attempt = 1

user = int(input("Guess the Number 1 to 100: "))

while(jackpot!=user):
    if(jackpot>user):
        print("Its Lower: ")
        user = int(input("Guess again the Number 1 to 100: "))

    else:
        print("Its Higher: ")
        user = int(input("Guess again the Number 1 to 100: "))

    attempt+=1

print("Congrats!!!! You Guess the Number. Your Attemps are: ",attempt, "/nJackpot number: ",jackpot)