from collections import deque
lista = deque([1, 2, 3])
print('deque:', lista)
lista.append(4)
print('deque añadiendo a la derecha es:')
print(lista)
lista.appendleft(6)
print('deque añadiendo a la izquierda es:')
print(lista)