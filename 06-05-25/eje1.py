'''ejercicio 
Desarrollla un programa que permita poblar unaa lista de
 tamanoo 50 osea (49 elementos ) 
 0 1 0 1 0 1 0 1 
 necesita un ciclo que se repita 
'''
numeros = []
for i in range(0, 50, 1):
   numeros.append(i % 2)

print(numeros)