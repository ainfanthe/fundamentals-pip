# tupla = (500, 18, 65)
# print(tupla[1])
from collections import namedtuple
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
Andres = Persona('Andres', 1.87, 75)

print(Andres.altura)
print(Andres[1])