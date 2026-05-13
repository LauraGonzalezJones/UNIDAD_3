#los primeros 5 sean perfectos  
''' todo lo que debe pedir una funcion es en los argumentos 
las funciones se adaptana  ala arquitectura de cualqeuier 
programa 
la funciones no deben llevar input 
la funciones van ejecutan y retornan 
si esta necesita 3 argumentos se piden
 investigar JSON es untipo de estructura que tranfiere cualquier tipo de 
datos y es universal 
'''
#los primeros 5 sean perfectos  

def es_perfecto(num):
    suma = 0

    for i in range(1, num , 1):
        if num % i == 0:
            suma = suma + i

    if suma == num:
        return True
    else:
        return False

def primeros_perfectos(n: int):
   mis_perfectos = []
   numero = 1
   cont = 1
   while cont <= 5:
      print(numero)
      if es_perfecto(numero):
         mis_perfectos.append(numero)
         cont = cont + 1

      numero = numero + 1

   return mis_perfectos
