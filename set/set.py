
record_list = []
flag = True
while flag:
    print("|-----------------------------------|")
    print("|1| Add new record.                 |")
    print("|-|---------------------------------|")
    print("|2| Search record by roll.          |")
    print("|-|---------------------------------|")
    print("|3| Edit record by roll.            |")
    print("|-|---------------------------------|")
    print("|4| Delete record by roll.          |")
    print("|-|---------------------------------|")
    print("|5| Enter 5 for exit                |")
    print("|-----------------------------------|")
    inp = int(input("Enter: "))
    
    if inp == 1:
        record = {}
        name = input("Enter the name: ")
        rollNum = input("Enter the Roll Number: ")
        record['name'] = name
        record['rollNum'] = rollNum
        record_list.append(record)
        
    elif inp == 2:
        roll = input("Enter the Roll Number: ")
        for i in record_list:
            if i['rollNum'] == roll:
                print(end="")
                print("|",i,"|")
            else:
                print("*****NOT FOUND*****")
    elif inp == 3:
        roll = input("Enter the ROLL NUMBER: ") 
        for i in record_list:
            if i['rollNum'] == roll:
                i['name'] = input("Enter NAME for Update: ")
                i['rollNum'] = input("Enter ROll NUMBER for Update: ")
                
    elif inp == 4:
        roll = input("Enter the ROLL NUMBER: ")
        for i in record_list:
            if i['rollNum'] == roll:
                record_list.remove(i)
                print("*****Deleted*****")
    elif inp == 5:
        flag = False
        print("******* EXIT *********")

    else:
        print("Wrong input")
 
