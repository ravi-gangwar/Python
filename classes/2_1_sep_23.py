x = 10
y = 20
x,y = y,x
print(x,y)
#########################################################################################
print(3/5)
#########################################################################################
if(id(x)==id(y)):                                                                       #
    print("y")                                                                          #
else:                                                                                   #
    print("w")                                                                          #
#########################################################################################
print(type([1,2,3,45,6,7]))
#########################################################################################
print("a"+"ab")
#########################################################################################
import keyword
print(keyword.kwlist)
#########################################################################################
a,b,c = 1,2,3
print(b,c,a)
#########################################################################################

a=10
b=10
print(id(a))
print(id(b))

print(a is b)
####################################

a = 4+7j
b= 5+8j

print(id(a))
print(id(b))
