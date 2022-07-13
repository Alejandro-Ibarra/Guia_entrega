import modulo_ejemplo
import functools
from Paquete_ejemplo.paquete_ejemplo2 import ejemplo_paquete
import os
from pathlib import Path
import struct

#3.	Escriba en un mismo código de ejemplo las sentencias condicionales y de iteración para cada estructura conocida del lenguaje: [if, elseif y else] [while y for].
mov = ["A", "D", "W", "S"]
while len(mov) < 4:
    movimientos(mov)
    def graficos_movimiento(char):
        if char == "A":
            direccion = "izquierda"
        elif char == "D":
            direccion = "derecha"
        elif char == "W":
            direccion = "arriba"
        else :
            direccion = "abajo"
        return direccion
    print(graficos_movimiento(input("Ingrese un caracter: ")))

    def movimientos(lista):
        for char in lista:
            print(graficos_movimiento(char))

#4.	Realice el código necesario para definir una clase
class personaje :
    def __init__(self, nombre, sexo):
        self.nombre = nombre
        self.sexo = sexo

    def setNombre(self, nombre):
        self.nombre = nombre
    def setSexo(self, sexo):
        self.sexo = sexo
    def getNombre(self):
        return self.nombre
    def getSexo(self):        
        return self.sexo


#5.	Realice el código necesario para instanciar dicha clase

person = personaje("Manwe", "M")

#6.	Realice un ejemplo en código donde se demuestre el encapsulamiento

class personaje :
    def __init__(self, nombre):
        self.nombre = nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre


#7.	Realice un ejemplo en código para herencia simple y múltiple

class personaje :
    def __init__(self, nombre):
        self.nombre = nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre

class otro_personaje:
    def __init__(self, vida):
        self.vida = vida
    def setVida(self, vida):
        self.__vida = vida
    def getVida(self):
        return self.__vida

class herencia_simple(personaje):
    def __init__(self, nombre, ataque):
        super().__init__(nombre)
        self.ataque = ataque
    def setAtaque(self, ataque):
        self.ataque = ataque
    def getAtaque(self):
        return self.ataque

class herencia_multiple(personaje, otro_personaje):
    def __init__(self, nombre, vida):
        super().__init__(nombre)
        self.vida = vida
    def setVida(self, vida):
        self.vida = vida
    def getVida(self):
        return self.vida


#8.	Realice un ejemplo en código que permita polimorfismo 

class atacar:
    def atacar (self):
        pass

class gerrero(atacar):
    def atacar(self):
        print("50 daño")

class mago(atacar):
    def atacar(self):
        print("30 daño")


#9.	Realice un ejemplo en código donde se utilicen los métodos especiales init, new, del, str y cmp.

class personaje :
    def __new__ (cls):
        return super().__new__(cls)
    def __init__(self, nombre):
        self.nombre = nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    def getNombre(self):
        return self.__nombre
    def __str__(self):
        return "Nombre: " + self.__nombre
    def __del__(self):
        print("Se ha eliminado")
    def __cmp__(self, other):
        if self.__nombre == other.__nombre:
            return 0
        elif self.__nombre > other.__nombre:
            return 1
        else:
            return -1
#10.Realice un ejemplo en código para el uso de diccionarios, cadenas y listas.

def ejemplo_diccionario():
    diccionario = {"nombre": "Manwe", "Ainur": "Guerrero", "poder": "20"}
    print(diccionario["nombre"])
cadena = {"El guerrero hace daño de 20"}
def ejemplo_lista():
    lista = ["pocion", "espada", "arco", "escudo"]
    print(lista[0])


#11.Realice un ejemplo en código para el uso de una función de orden superior
def iniciar_juego(juego):
    def elegir_personaje(personaje):
        print("Elegiste: " + personaje)
    def elegir_arma(arma):
        print("Elegiste: " + arma)
    juego = {"personaje": elegir_personaje, "arma": elegir_arma}
    
    return juego


#12.Realice un ejemplo en código para cada función de: map, filter y reduce

def multiplicacion(x):
    return x * 2
l = [1, 2, 3, 4, 5]	
multi = map(multiplicacion, l)
for i in multi:
    print(i)

numeros = [0, 4, 6, 13, 16, 13]
resultado = filter(lambda x: x % 2 != 0, numeros)
print(list(resultado))
  
resultado2 = functools.reduce(lambda x, y: x if x > y else y, numeros)
print(resultado2)

#13.Realice un ejemplo en código para el uso de una función lambda

numeros = [0, 4, 6, 13, 16, 13]
resultado = filter(lambda x: x % 2 == 0, numeros)
print(list(resultado))

#14.Realice un ejemplo en código para el uso de una list comprehension
def comprehension(lista):
    l = [1, 2, 3, 4, 5]	
    j = [4, 6, 1, 7, 4]
    list_comp = [x * 2 for x in l
                 if x * 2 in j]
    print(list_comp)

#15.Realice un ejemplo en código para el uso de una expresión generadora
def comprehension(lista):
    l = [1, 2, 3, 4, 5]	
    j = [4, 6, 1, 7, 4]
    list_comp = (x * 2 for x in l
                 if x * 2 in j)
    print(list_comp)

#16.Realice un ejemplo en código para el uso de una función decoradora

def deco(f):
    def fun_deco(a, b):
        print("Función suma() invocada")
        return f(a, b)
    return fun_deco
@deco
def suma(a, b):
    return a + b
print(suma(7, 5))

#17.Realice un ejemplo en código para el tratamiento de una excepción

def ingresar_numero():
    try:
        numero = int(input("Ingrese un numero: "))
        return numero
    except ValueError:
        print("Error, ingrese un numero")
        return ingresar_numero()
#18.Genere un código que permita la creación y el uso de un módulo.

modulo_ejemplo.ejemplo()


#19.Agregue el uso de paquetes al código anterior.
ejemplo_paquete()

#20.Genere un código para la creación, apertura, grabación, lectura y cierre de un archivo
    #a.	de texto
    #b.	de datos binarios
directorio = f"{os.path.dirname(__file__)}"
archivo = open(f"{directorio}archivo.txt", "w")
archivo = open(f"{directorio}archivo.txt", "r")
archivo.write("Hola mundo")
archivo.close()
data = Path('ejemplo.bin').read_bytes() 
multiple = struct.unpack('ii', data[:8])
print(multiple)

#21.Genere el código para tratar los errores de la gestión de archivos del punto anterior.
try:
  archivo = open(f"{directorio}archivo.txt", "r")
except FileNotFoundError:
  print(f"Este es un ejemplo de manejo de error")

#22.Genere un ejemplo donde aplique expresiones regulares en la lectura (Línea a línea) de un archivo 
# X (Por ejemplo, encontrar direcciones de email u otro patrón que usted desee), 
# guarde las líneas que contienen su patrón en un archivo y en otro las líneas que no lo contiene.


#23.Genere códigos de ejemplo utilizando cada una de las bibliotecas: Pygame, RE, Collections, NumPy,
#  SQLAlchemy, Request y Pillow.


#24.Genere el código para que un perceptrón pueda aprender las compuertas AND, OR, NOT, XOR y XNOR.


#25.Diseñe el código para que un vehículo arduino/micro:bit pueda aprender a evitar obstáculos  


