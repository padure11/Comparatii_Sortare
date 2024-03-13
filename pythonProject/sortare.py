import random
import time
import sys

sys.setrecursionlimit(10000000)

total_numbers = 20000



listuta1 = []
listuta2 = []
listuta3 = []
listuta4 = []
listuta5 = []

for _ in range(total_numbers):
    x = random.randint(0,1000)
    listuta1.append(x)
    listuta2.append(x)
    listuta3.append(x)
    listuta4.append(x)
    listuta5.append(x)

# Bubble Sort


def bubblesort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


start_time = time.time()

lista1_sort = bubblesort(listuta1)

print((time.time() - start_time))



# Sortare prin insertie


def insertion_sort(lista):
    for i in range(1, len(lista)):
        val = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > val:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = val

    return lista


start_time = time.time()

lista2_sort = insertion_sort(listuta2)

print((time.time() - start_time))



# Sortare prin selectie


def selectionsort(lista):
    for i in range(0, len(lista)):
        k = i
        for j in range(i + 1, len(lista)):
            if lista[k] > lista[j]:
                k = j
        if k != i:
            lista[i], lista[k] = lista[k], lista[i]

    return lista


start_time = time.time()

lista3_sort = selectionsort(listuta3)

print(time.time() - start_time)



# Sortare Rapida

def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2]

    stanga = []
    dreapta = []
    mijloc = []

    for i in lista:
        if i < pivot:
            stanga.append(i)
        if i > pivot:
            dreapta.append(i)
        if i == pivot:
            mijloc.append(i)

    return quicksort(stanga) + mijloc + quicksort(dreapta)


start_time = time.time()
lista4_sort = quicksort(listuta4)

print(time.time() - start_time)



# #Sortare prin Interclasare


def mergesort(lista):
    if len(lista) <= 1:
        return lista

    mijloc = int(len(lista) // 2)
    lista_stanga = (mergesort(lista[:mijloc]))
    lista_dreapta = (mergesort(lista[mijloc:]))
    return interclasare(lista_stanga, lista_dreapta)


def interclasare(lista_stanga, lista_dreapta):
    i = 0
    j = 0

    mergelist = []

    while i < len(lista_stanga) and j < len(lista_dreapta):
        if lista_stanga[i] < lista_dreapta[j]:
            mergelist.append(lista_stanga[i])
            i = i + 1

        else:
            mergelist.append(lista_dreapta[j])
            j = j + 1

    mergelist = mergelist + lista_stanga[i:]
    mergelist = mergelist + lista_dreapta[j:]

    return mergelist


start_time = time.time()

lista5_sort = mergesort(listuta4)

print(time.time() - start_time)
