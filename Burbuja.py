import random
#esta funcion se utiliza para crear valores aleatorios en el codigo

def burbuja(arr):
    n = len(arr) #n almacena el largo del arreglo, es decir, la cantidad de datos en el arreglo
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #lo que se hace en el condicional solamente en hacer swap en cada uno de los valores del arreglo si es mayor el valor de la derecha
                #que el de la izquiera

# Generar una lista de 10 números aleatorios
datos = [random.randint(1, 100) for _ in range(10)]

print("Lista original:", datos)

# Ordenar la lista utilizando el método de ordenamiento de burbuja
burbuja(datos)

print("Lista ordenada:", datos)
