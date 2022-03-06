#Counting Sort
import numpy
from time import time
import random
import pylab as pl

#Generar lista aleatoria
def lista(n):
    l = []
    for x in range(0,n):
        l.append(random.randrange(100))
    return l

lista = list(lista(10))
print("Lista en desorden")
print(lista)
start_t = time()
#Determinar ocurrencias de cada numero de la lista
occurs = list(numpy.bincount(lista))
print("\nOcurrencias de cada numero en la lista")
print(occurs)
#sumar elementos de la lista en base a la cantidad de ocurrencias del numero con el indice anterior
sums = list(occurs)
for x in range(1, len(occurs)):
    sums[x] += sums[x-1]
print("\nSumatoria")
print(sums)
#ordenar
ordenada = [0]*(len(lista))
i = len(lista) - 1
while i >= 0:
    ordenada[sums[lista[i]] - 1] = lista[i]   #Se toma el indice encontrando el valor en la lista para pasarlo como indice de los valores de la sumatoria -1
    sums[lista[i]] -= 1 #Se resta uno al valor del indice para ajustar los indices
    i-=1
print("\nLista en orden")
print(ordenada)
print("\nCantidad de elementos a ordenar: ", len(lista))
print("Tiempo de ejecucion: ", time()-start_t)
print("\nSe mostrara la grafica resultante de la complejidad en base a los valores de tiempo vs cantidad de elementos")
t=[0, 0.0023, 0.0029, 0.024, 0.0953, 0.1913]
k=[0,10,100,1000,5000,10000]
pl.plot(t,k)
pl.show()