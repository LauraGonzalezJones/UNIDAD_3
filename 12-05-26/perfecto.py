"""
Crea una funcion para detectar numero perfectos, es_perfecto (numero)
si es verdadero o falso 
 """
def es_perfecto (numeros):
    numero = 0 
suma_divesores = 0 
numero = int (input("ingresa un numero para verificar si es perfecto "))


for i in range (1,numero ):                         
     if numero % 1 == 0: