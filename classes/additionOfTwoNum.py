def add_rec(a, b):
    if b == 0:
        return a
    else:
        return add_rec(a + 1, b - 1)

r = add_rec(11, 980)
print(r)
