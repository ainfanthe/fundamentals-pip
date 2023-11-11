
# Los generadores, valga la redundancia, van generando en tanto se vaya solicitando
def funcion():
    lista = []
    for i in range(1,5):
        lista.append(i * 10)
    return lista

def generador():
    for i in range(1, 5):
        yield i * 10 # esto es más ecónomico en términos de espacio

print(funcion())
print(generador())

g = generador()
print(next(g))