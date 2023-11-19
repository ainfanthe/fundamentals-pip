"""
Insertion sort algorithm
"""
def insertion_sort(arr): # Acepta una lista como argumento
    for i in range(1, len(arr)): # Iteramos desde la posición 1 hasta la longitud de la lista
        # En cada iteración se van comparando uno a uno los elementos para ir creando la lista ordenada
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j +1] = arr[j]
            j -= 1
            arr[j + 1] = key
        # Al haber dos bucles, contiene una complejidad algoritmica de O(N^2)
lista = [11, 13, 5, 12, 8]
insertion_sort(lista)
print('lista ordenada: {}'.format(lista))