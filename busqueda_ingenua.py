import time
import random


def busqueda_ingenua(lista,objetivo):
    for i in range(len(lista)):
        if lista[i]==objetivo:
            return i
    return -1


lista=[1,2,5,6,12,20]
print(busqueda_ingenua(lista,12))