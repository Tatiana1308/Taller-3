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
