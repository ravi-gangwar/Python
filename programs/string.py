s = 'AAABBBBCCCCCCCCCDA'
#output = 3A3B3C

n = len(s) - 1

f = s[0]
for i in s:
    if(f != i):
        print(s.count(f), end="")
        print(f, end="")
    f = i
print(s.count(s[n]), end="")
print(f)
