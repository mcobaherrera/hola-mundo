# Calculadora básica: Escribe un programa que realice operaciones básicas (suma, resta, multiplicación y división) 
# entre dos números introducidos por el usuario.

opcion=int(input("escoja opcion: "))
print(f"1.suma\n2.resta\n3.multiplicacion\n4.division\n5.salir")
def operacion(a,b):
  if opcion==1:
    return(a+b)
  elif opcion==2:
    return(a-b)
  elif opcion==3:
    return(a*b)
  elif opcion==4:
    return(a/b)

if opcion==5:
  print("gracias por usar la calculadora")
else:
  num1=int(input("ingrese numero: "))
  num2=int(input("ingrese numero: "))
  resul=operacion(num1,num2)
  print("el resultado es: ",resul)

