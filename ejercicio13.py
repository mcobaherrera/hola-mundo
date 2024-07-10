# Contar vocales: Escribe un programa que cuente el número de vocales en una cadena introducida por el usuario.
cadena=input("ingrese texto: ")
contador=0
for i in cadena:
  if i.upper() in ("A","E","I","O","U"):
    contador +=1
print("el numero de vocales es: ",contador)
