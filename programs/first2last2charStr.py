s = input("Enter String: ")
if(len(s) > 2):
    FirstTwo = s[0:2:1]
    LastTwo = s[-1:-3:-1]
    LastTwo = LastTwo[-1::-1]
    print(FirstTwo+LastTwo)
else:
    print("Empty String")