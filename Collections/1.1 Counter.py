# Collections es parte de las bibliotecas integradas en python
# from collections import [elemento], ayuda a manipular estructuras de datos de manera eficiente
numeros = [8,5,4,2,5,6,7,8,4,2,1,3] # suponiendo que deseamos saber cuantas veces se repite cada uno de los números
# podría emplearse un loop que recorra los elementos para asignarles dentro de un diccionario, etc
# collections realiza esto de manera más sencilla empleando counter. E.g:

from collections import Counter
print(Counter(numeros))
# Counter({8: 2, 5: 2, 4: 2, 2: 2, 6: 1, 7: 1, 1: 1, 3: 1})
# Funciona también para contar strings
serie = Counter([1,1,1,2,3,2,3,4,5,5,5,5,6,6,7])
print(serie.most_common(1))
print(list(serie))