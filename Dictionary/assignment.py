# d = {"zeeshan" : 78, 'sumit':56, "amitash":90, "sonu":45}

# for k in d.items():
#     print(k)
#     print(type(k))


loop = 'y'
li = []
while(loop == 'y'):
    d = dict()
    n = input("Enter you name: ")
    d['name'] = n
    a = input("Enter the age: ")
    d['age'] = a
    li.append(d)
    loop = input("For continue prees 'y' else 'f': ")
print(li)