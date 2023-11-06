def f1(**a):
    if len(a)==0:
        print("zero")
    elif len(a)==1:
        print("One")
    elif len(a)==2:
        print("Two")
    else:
        print("OK")

f1(name="amit",age=67)