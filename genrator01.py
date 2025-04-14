def gen():
    yield 'A'
    yield 'B'
    yield 'C'
g=gen()
print(type(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
