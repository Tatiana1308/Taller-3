#TALLER
# crear un programa que pida un numero al usuario y:
# 1. Imprima los numeros impares entre -numero y numero
# 2. Imprima los numeros numeros primos entre 0 y numero*100
# El programa debe garantizar que el usuario ingrese un numero positivo mayor que 0

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_impares_entre(a, b):
    print("Números impares entre", a, "y", b, ":")
    for i in range(a, b+1):
        if i % 2 != 0:
            print(i, end=" ")
    print()

def imprimir_primos_entre(a, b):
    print("Números primos entre 0 y 100:")
    for i in range(a, b+1):
        if es_primo(i):
            print(i, end=" ")
    print()

while True:
    try:
        numero_a = int(input("Ingrese el primer número positivo mayor que 0: "))
        if numero_a <= 0:
            raise ValueError("El número debe ser positivo y mayor que 0.")
        break
    except ValueError as e:
        print(e)

while True:
    try:
        numero_b = int(input("Ingrese el segundo número positivo mayor que 0: "))
        if numero_b <= 0:
            raise ValueError("El número debe ser positivo y mayor que 0.")
        break
    except ValueError as e:
        print(e)

imprimir_impares_entre(numero_a, numero_b)
imprimir_primos_entre(0, 100)
# while
#while <condicion verdadera>:
# cuerpo del ciclo
# condiciones son: expresiones boleanas (or, and) y operaciones de comparacion
# operaciones de comparacion
#  ciclos controlados por un contador entero

i= 0
k= 0

while i<10:
    print("ciclo")
    # importante controlar el valor del contador
    i=i #es equivalente (i+=1)

import random
a=0
while a != 5:
    a=random.randint(1,10) #por evento

print("se acabo")

a=0
while 1==1:
    a=int(input("ingrese un numero")) #por variable
    if a==10:
        break

#for: se utiliza para recorrer un "iterable"
#una lista, tupla, diccionario, etc
        
#lista: conjunto de variables organizadas en espacios consecutivos de memoria. A las que 
# se les asigna un unico nombre, se diferencian por la posicion que ocupan respecto al priemer
#elementos de una lista

miLista=[1, True, "textos",3.98]
miLista=[]

# en python todos son objetos, tiene metodos y atributos
print(miLista)

print(miLista)
miLista.insert(0,"Hola") #remueve el item en el indice que yo le pida
print(miLista)

print(miLista)
miLista.sort(45) #ordena la lista de manera descendente o ascendente
print(miLista)

print(miLista)
miLista(len(0,"Hola")) #mide la longitud de un iterable
print(miLista)

# Tupla: lista inmutable
miTupla=(2,45,6,8,9,10)

#for: ciclo para recorrer iterables. el cuerpo se repite la cantidad de elementos que tenga el iterable. 
#en cada ciclo se guarda el valor.
#estructura del FOR en python:
#for<variable_donde_guardo_el _elemento in iterable:

for x in miLista:
    print(x)
    if x>50:
        print("grande")
#si solo utilizo el iterable para definir la cantidad
# de repeticiones entonces no es necesaria la variable

for_ in miLista:
print("ciclo")

#si no tengo un iterable puedo usar la funcion 
#range() para generar una secuencia de numeros

for x in range(-10,10):
    print(x)

#Taller
# crear un programa en consola que pida un numero al usuario y 
# 1. imprima los numeros impares entre numero y numero
# 2. Imprima los numeros primos entre 0 y 100
# el programa debe garantizar que el usuario ingrese un numero positivo >0

#entrega antes de las 4 en el repositorio
