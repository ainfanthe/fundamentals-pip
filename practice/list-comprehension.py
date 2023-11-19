# EL metodo .remove() de las listas tiene una complejidad algoritmica lineal
# Cada vez que se elimina un elemento con .remove() se genera una lista con los elementos restantes
# Lo anterior produce un consumo extendido de memoria


# Eliminar los impares del siguiente ejercicio usando como apoyo la lista auxiliar
# Debe hacerse en -1seg, no se emplea .remove()
lista_original = list(range(1, 1000001))
lista_auxiliar = set(1, 1000001, 2)

lista_nueva = [element for element in lista_original
               if element not in lista_auxiliar]