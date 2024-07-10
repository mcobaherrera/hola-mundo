# Número mayor: Escribe un programa que pida tres números al usuario y determine cuál es el mayor.

num1=(input("ingrese numero1: "))
num2=(input("ingrese numero2: "))
num3=(input("ingrese numero3: "))
lista=[]
lista.append(int(num1))
lista.append(int(num2))
lista.append(int(num3))
print("el mayor es: ",max(lista))
