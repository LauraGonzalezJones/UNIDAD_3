'''
Una lista para poder guardar  varios elementos 


Estructura de datos mutables y estaticas 

'''
''' 
Las lista'''
#          0  1  2  3  4
numeros = [2, 5, 1, 4, 7] #esto e un elemnto y el indice es l

print(f"Elemento índice 2 -> {numeros[2]}")


'''print("Recorrer con ciclo for")
#elementos 
i = 0 
for num in numeros: # en el cicl
   if num % 2 == 0:
     print(f"{num} es par")
print(num) '''


#Recorrer con while
'''print("Elementos de la lista ->", len(numeros))
print("Recorrer con ciclo while")
i = 0
while i < len(numeros):
   num = numeros[i]
   if num % 2 == 0:
      print(f"{num} es par y está en el índice {i}")

   print(num)
   i = i + 1

print(numeros)'''
''' saber lo que es un  cola , fila y estructura de datos  '''

#metodos de una lista acciones  esta tiene atributos 

edades = []
edades.append(48)
edades.append(27)
edades.append(26)
edades.append(28)
edades.append(29)
edades.append(30)
print(edades)





# insertar  
edades.insert ( 2, 36) # inserta el valor en el indice 2 
print (edades)
#elimina elementos 
#edades.remove(28) #no lo usen nunca 
#ya aque no  trabajaremos con esta info 
#print(edades)

#eliminar elemento del  indice que indicamos en este caso 4
del edades [4]
print (edades)

# pop  enntrega el elemnto y lo elimina de la lista 
elemento_cero = edades.pop (0)
print ("SE elimino el elemento del indice 0 su valor era ->,", elemento_cero)



edades [2]

print(edades)

''' investigar vectores, arreglos, matrices 


ejercicio 
Desarrollla un programa que permita poblar unaa lista de
 tamanoo 100 osea (99 elementos ) 
 0 1 0 1 0 1 0 1 
 necesita un ciclo que se repita 




python es interpretado y las funciones van siempre arriba 









 
'''