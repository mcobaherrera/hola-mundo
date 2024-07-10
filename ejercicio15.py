#  Factorial de un número: Escribe un programa que calcule el factorial de un número introducido por el usuario.

def factorial(a):
    acum=1
    for i in range(1,a+1):
        acum= i * acum
    return acum

num=int(input("ingrese numero que desea el factorial: "))
print("el factorial es: ",factorial(num))
