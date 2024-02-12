class A:
    def __init__(self, a):
        self.a = a
    
    # adding two objects
    def __add__(self, o):
        return self.a + o.a

obj1 = A(2)
obj2 = A(3)

result = obj1 + obj2

print(result)