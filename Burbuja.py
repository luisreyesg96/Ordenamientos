import random

def burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generar una lista de 10 números aleatorios
datos = [random.randint(1, 100) for _ in range(10)]

print("Lista original:", datos)

# Ordenar la lista utilizando el método de ordenamiento de burbuja
burbuja(datos)

print("Lista ordenada:", datos)
