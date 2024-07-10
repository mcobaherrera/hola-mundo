# Números primos: Escribe un programa que determine si un número introducido por el usuario es primo.
def es_primo(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

num=int(input("ingrese numero para comprobar si es primo: "))
if es_primo(num):
    print("el numero ingresado SI es primo")
else:
    print("el numero ingresado NO es primo")
