n=input("Name\n")
n=n.title()
match n:
    case "Ravi":
        print("Yes")
    case _:
        print("No")