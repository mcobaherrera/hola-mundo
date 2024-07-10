# Sumar números hasta un límite: Escribe un programa que sume todos los números naturales hasta un número límite introducido por el usuario.

num=int(input("ingrese numero limite: "))
acum=0
for i in range(num+1):
  acum=acum+i
print("la suma es: ",acum)
