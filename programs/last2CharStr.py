s = input("Give a string: ")
if len(s) > 1:
    r = s[-1:-3:-1]
    r = r[-1::-1]
    print(r*4)
else:
    print("Not Valid!")