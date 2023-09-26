a = 'India'
b = 'Pakitan'

# print(min(a,b)) # because I comes before the P so;

c = "india"
# print(min(a,c)) # Because small i comes afetr the Capital I in the dictionary

# Methods of Strings

#1 Capitlize
print(c.capitalize())

#2 Upper()
print(c.upper())

#3 Lower
print(c.lower())

#4 Casefold
c = 'raVi GAnGwAR'
print("CaseFOLD->", c.casefold())


#lower to upper and lower to upper
c = 'RAVI gangwar'
print(c.swapcase())

c = "RavI GanGWar"
print(c.swapcase())


#it will remove white space from the starting of the string
c = "     RAvi GAngwar"
print(c.strip())


#trim left space 
c = "    Ravi Gangwar   "
print(c.lstrip())

#trim right space 
c= "    ravi gangwar   "
print(c.rstrip())


#replace the word 
c = "Ravi"
print(c.replace("R", "A"))

# count of the letter in the word
c  ="Hello"
print(c.count("l"))


c = "ravi gangwar"
print(c.isalnum())
print(c.isalpha())
print(c.isdecimal())
print(c.isascii())


#return a List 
c = "Hello, my name is Ravi"
print(c.split())

c = "Hello world"
print(c.endswith('ld'))

c = "My age is" + ' 19'
print(c)

#insert in the string a integer value 
s = 12
cl = 8
c = "My age is {} and my class is {}"
print(c.format(s, cl))