# Strings Are Inmuteable
s = "Ravi 'Gangwar'" # String
a = '''Ravi gangwar 
Branch IT B
Subject is PYTHON'''#Multi line String

print(a[-1]) #slicing of String
print(a[0])
print(a[0:4])

c = "Hellow World"

print(c[7: 12])
v = '''My name is Ram I am in Class Six'''

print(v[-3:])
print(a[:])
print(a[0: :1]) 
print(v[-1: : -1]) # third argument negative only 


# Deleing String

s = "Hello World"

del s

# print(s)


# operations in string


print("RAM"*10)
print("SEETA" + "RAM")



for i in range(1, 10):
    print('*'*i)