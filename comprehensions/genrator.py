def gen(m):
    for i in range(1,m):
        yield i*i

a=list(gen(11))
b=gen(5)
print(b)
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))