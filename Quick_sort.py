import random #el modulo random se utiliza para generar numeros aleatorios


def quick_sort(arr):
    if len(arr) <= 1:  #condicional, en caso de que sea menor a 1, no hace nada
        return arr
    pivot = arr[len(arr) // 2] #se le da valor al pivote con el valor medio de la lista
    left = [x for x in arr if x < pivot] #se crea una lista de todos los valores menores que el valor pivote
    middle = [x for x in arr if x == pivot] #lista con valores iguales al pivote
    right = [x for x in arr if x > pivot] #lista con valores mas grandes que el pivote
    return quick_sort(left) + middle + quick_sort(right) #retorna las listas ordenadas y concatenadas

# Generar una lista de 10 números aleatorios
datos = [random.randint(1, 100) for _ in range(10)] #se generan 10 datos aleatorios y se guardan en "datos"

print("Lista original:", datos) #imprime la lista original

# Ordenar la lista utilizando el algoritmo de QuickSort
datos_ordenados = quick_sort(datos) #llama a la funcion de ordenamiento

print("Lista ordenada:", datos_ordenados) #imprime los datos ordenados
datos_ordenados = quick_sort(datos)

print("Lista ordenada:", datos_ordenados)
