"""
Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final.
"""

import random

def crearMatrizRandom():
  lista = []
  matriz_random = []
  for i in range (1,6):
    lista = []
    for j in range (1,6):
      lista.append (random.randint(1,10))  #utilizo valores del 1 al 10 para la prueba
    matriz_random.append(lista)
  return matriz_random

    
def print_matriz(matriz):
  rango = len(matriz)
  for i in range(rango):
    for j in range(len(matriz[i])):
      print(matriz[i][j], end= "\t")
    print()


def encontrarSecuencia(matriz):
    for i in range(len(matriz)): # dentro de este for se revisa de manera horizontal
        lista = [] #utilizo lista aparte de la matriz para comprobar si hay consecutivos
        indices = []
        for j in range(len(matriz)):
            if not lista or lista[-1] == matriz[i][j] - 1:
                lista.append(matriz[i][j])
                indices.append([i, j])
            else:
                lista.clear()
                lista.append(matriz[i][j])
                indices.clear() #limpieza de la lista de indices en caso de no encontrar consecutivos
                indices.append([i, j])
            if len(lista) == 4: #si encuentra coincidencias, retorna los indices 
                return indices
    for i in range(len(matriz)):          # dentro de este for se revisa de manera vertical
        lista = []  #utilizo lista aparte de la matriz para comprobar si hay consecutivos
        for j in range(len(matriz)):
            if not lista or lista[-1] == matriz[j][i] - 1:
                lista.append(matriz[j][i])
                indices.append([j, i])               
            else:
                lista.clear()     #si no se encuentra nada, se elimina la lista para hacer nuevamente la comprobacion
                lista.append(matriz[j][i])
                indices.clear()     #limpieza de la lista de indices en caso de no encontrar consecutivos
                indices.append([j, i])
            if len(lista) == 4:
                return indices #si encuentra coincidencias, retorna los indices 
    return False # si no encontro nada, retorna un boolean
          
b = crearMatrizRandom()

print_matriz(b)


print (encontrarSecuencia(b))

#encontrarSecuencia(b)