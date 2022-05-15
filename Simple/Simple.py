"""
Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
elementos. retornar la lista.

Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada.
"""

import random

def lista_diccionarios():
  lista = []
  diccionario1 = {} # el id va a ser asignado dentro del ciclo, cada posicion de el iterador "i" va a corresponder a un ID
  tamaño_lista = 10

  for i in range (1,tamaño_lista+1): #arranca la lista desde 1 para no tener un ID "0"
      diccionario1 = {"id":i , "edad":random.randint(1,100)} #i == id , y utilizo la libreria random para generar un numero entero donde 1<= n <=  100
      lista.append(diccionario1) #agrego el diccionario terminado a la lista

  return lista

def ordenar_diccionario(a): #donde "a" es la lista retornada por la funcion "lista_diccionarios()"
  elementos_lista = len(a)
  mayor=-1
  menor=101 #inicializo de manera arbitraria el menor y el mayor, con valores que para que la primer edad ingresada sea la mayor y la menor a la vez, pero dentro del rango
  aux = 0

  lista_ordenada = sorted(a, key=lambda p: p["edad"], reverse=True) # utilizo sorted con la funcion lamda para ordenarlos, (agrego "reverse=True" para que ordene de mayor a menor)
          
  for i in range (elementos_lista):
    b = dict(a[i]) #separo el primer elemento (el primer diccionario) para trabajar con sus valores (B = {id="" , edad=""})
    edad = b['edad']
    if edad > mayor:
      mayor = edad          #busco mayores y menores mediante condicionales
      id_mayor = b['id']
    if edad < menor:
      menor = edad
      id_menor = b['id']
  print (f"El id del menor: {id_menor} La edad: {menor}\nEl id del mayor: {id_mayor},La edad: {mayor}")


  return lista_ordenada
     
a = lista_diccionarios()
print (a)
print(ordenar_diccionario(a))
