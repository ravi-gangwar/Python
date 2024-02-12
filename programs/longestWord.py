s = input("Give String: ")
l = s.split()
max = 0
for i in l:
    if(max < len(i)):
        max = len(i)
        m = i
print(m)
