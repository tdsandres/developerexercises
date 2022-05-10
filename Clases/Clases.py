"""
Escribir una clase en python llamada círculo que contenga un radio, con un método que
devuelva el área y otro que devuelva el perímetro del círculo.
Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
usuario e impidiendo la instanciación.
Si printeamos el objeto creado debe mostrarse una representación amigable.
El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación.
Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0
"""

from math import pi

class Circulo:
  def __init__(self,radio):
    self.radio = radio

  def areaCirculo(self):
    area = pi * self.radio ** 2
    return area

  def perimetroCirculo(self):
    perimetro = 2 * pi * self.radio
    return perimetro
  

  
r = float(input("Ingrese el radio del circulo: "))

while r<=0:
  r = float(input("ERROR - Un circulo no puede tener un radio menor o igual a 0 | Ingrese el radio nuevamente: "))

radio = Circulo(r)

print(f"El area del objeto Circulo con radio {r}cm es: ~{radio.areaCirculo():.2f}cm^2 y el perimetro es: ~{radio.perimetroCirculo():.2f}cm")

n = int(input("MULTIPLICAR CIRCULO | ingrese 'n' (valor para multiplicar el radio): "))
while n<=0:
  n = float(input("ERROR - Un circulo no puede tener un radio menor o igual a 0 | Ingrese el radio nuevamente: "))
nuevoCirculo = Circulo(r*n)
print(f"El area del nuevo Circulo con radio {r*n}cm es: ~{nuevoCirculo.areaCirculo():.2f}cm^2 y el perimetro es: ~{nuevoCirculo.perimetroCirculo():.2f}cm")
