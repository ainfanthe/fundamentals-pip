# dic = {'uno':'verde', 'dos':'azul', 'tres':'rojo'}
# print(dic['dos'])
from collections import defaultdict
dic = defaultdict(lambda: 'nada') 
# en caso de que no exista una clave solicitada, le asigna o crea una clave llamada 'nada'
dic['uno'] = 'verde'
print(dic['dos'])

print(dic)
