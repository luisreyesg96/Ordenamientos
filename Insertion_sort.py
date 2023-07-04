
import random
#esta funcion se define para crear datos random en el codigo

def insertion_sort(arr):
    n = len(arr) #definimos n, la cual almacena la cantidad de datos que tenemos en el arreglo
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generar una lista de 10 números aleatorios
datos = [random.randint(1, 100) for _ in range(10)]

print("Lista original:", datos)

# Ordenar la lista utilizando el método de ordenamiento por inserción
insertion_sort(datos)

print("Lista ordenada:", datos)
