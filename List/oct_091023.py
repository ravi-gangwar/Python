# # list 

# list1 = list()

# list2 = [] # EMPTY LIST 

# list3 = [1,2,3,1.3, "LIST"]

# print(list3)

# list3[0] = 100

# print(list3)


data = [786, 'abc', 'a', 123.5]
# Array.index(element) to find index of element

# print("Index of 123.5: ", data.index(123.576)) // error
print("Index of 123.5: ", data.index('a'))


# list.insert(index, element)

data.insert(0, 4)


data1 = [1,3,"Ravi"]

# print(data + data1)  # ADD TO LIST 

data3 = [1,2,3,2,2,2,2,2,2]

#Count the number of occurances // array.count(element)

print(data3.count(2))

# Extend 

# print(data1.extend(data3))
# print(data1)

# Append

# print(data1.append(data3))
# print(data1)






# del" can delete any obj in python 

# del data

# print(data) # Error





# from collections import Counter

# list1 = [1,2,2,3,3,4,4,5,5,5,7]

# print(Counter(list1))


# data1.sort()
print(data1)

data3.sort()
print(data3)


data4 = [343, 32, 44, 54, 33, 43, 23, 22]

data5 = sorted(data4, reverse=True) # sorted function create new list but sort can not create new list it changes in original list
print(data5)

data5.remove(343);

print(data5)

list1 = [1001, 5555]

print(max(list1))

print(min(list1))

print(list1*2)

print(id(list1), id(data1))
print(list1 == data1)




data6 = ["Ram"]
data7 = ["Ram"]

print(data6 == data7)

data6 = data7

# e=print(data6.pop())
# print(e)

# e=list1.pop(1)
# print(e)


data6[0] = "sita"
print(data7)
