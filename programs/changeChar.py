s = input("Give String: ")
l = list(s)
f = s[0]
i = 1
for i in range(1, len(l)):
    if f == l[i]:
        l[i] = "$"
for i in l:
    print(i, end="")
