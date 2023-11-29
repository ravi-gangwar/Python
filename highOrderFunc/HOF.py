def square(x):
    return x * x

def cube(x):
    return x**3

def operation(func, n): #HOF 
    return func(n)


result = operation(square, 5)
print(result)
result = operation(cube, 5)
print(result)


