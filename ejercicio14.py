# Palíndromo: Escribe un programa que determine si una cadena introducida por el usuario es un palíndromo.
cadena=input("ingrese texto: ")
invierta = cadena[::-1]
if cadena == invierta:
  print("Es palindriomo")
else:
  print("NO Es palindriomo")
