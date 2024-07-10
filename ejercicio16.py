# Generar números aleatorios: Escribe un programa que genere y muestre 5 números aleatorios entre 1 y 100.
import random
num=0
lista=[]
for i in range(5):
  numero = random.randint(1, 100)
  print(numero)
