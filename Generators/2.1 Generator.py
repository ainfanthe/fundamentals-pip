def generador():
    x = 1 
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = generador()
print(next(g))
print(next(g))
print(next(g))