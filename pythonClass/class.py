class smallVal (Exception):
    def __init__(self, msg):
        self.msg = msg
    
class largeVal (Exception):
    def __init__(self, msg):
        self.msg = msg
try:
    a = int(input("Enter a number: "))
    if a < 10:
        raise smallVal("Small Value")
    if a > 10:
        raise largeVal("Large Value")
    else:
        print("Valid Value")
        
except smallVal as e:
    print(type(e.msg))
    for i in e.msg:
        print(i, end="")
    print("\n")
except largeVal as e:
    print(type(e.msg))
    for i in e.msg:
        print(i, end="")
    print("\n")
