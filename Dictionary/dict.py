d = {"name":"Ravi gangwar", "section":"Elite II", "rollNumber": 2212973, "branch":"IT"}
print(d)
print(d['name'])

#deleting the keys 
del d['rollNumber']
print(d)

#iterating the dictionary 

for k, v in d.items():
    print(k,v)

#updating the values
d['name'] = "Ravi"
print(d)

#sorting in the dictionary on the basis of values
for v in sorted(d.values()):
    print(v)

#sorting in the dictionary on the basis of keys
for k in sorted(d.keys()):
    print(k)

#reverse sorting 
for k in sorted(d.keys(), reverse=True):
    print(k)

#copy of dictionary

nd = d.copy()
print('Copy: ',nd)

# clear()        =>	Removes all the elements from the dictionary
# copy()        =>	Returns a copy of the dictionary
# fromkeys()    =>	Returns a dictionary with the specified keys and value
# get()	        =>  Returns the value of the specified key
# items()       =>	Returns a list containing a tuple for each key value pair
# keys()        =>	Returns a list containing the dictionary's keys
# pop()	        =>  Removes the element with the specified key
# popitem()     => 	Removes the last inserted key-value pair
# setdefault()  =>	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()      =>	Updates the dictionary with the specified key-value pairs
# values()      =>	Returns a list of all the values in the dictionary