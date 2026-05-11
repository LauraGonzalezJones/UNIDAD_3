''' 
en los ciclos se utiliza inicializacion, condicion y incremento

en el caso del ciclo for x in range( 1,3,2 ) en la inicializacion es 1, 
la condicion es 3 y el incremento es 2, entonces el ciclo se ejecutara mientras la variable i sea menor que 3, y en cada iteracion se incrementara en 2, entonces el ciclo se ejecutara una sola vez, ya que despues 
de la primera iteracion i sera igual a 3, y la condicion ya no se cumplira.  
 #todo lo que hace el for lo puede hacer el  while 

'''


for x in range( 0, 11, 1 ): # el primer numero es la inicializacion, 
    #el segundo numero es la condicion y el tercer numero es el incremento 
    print(x)

''' ejercicio desarrolle un programa que permita ingresar 5 numeros y 
al finalizar retorne cuantos numero pares ingreso el ux 
nota: solo deben considerar numeros positivos, el programa debe validar que el numero
 ingresado sea positivo, si el numero es negativo debe mostrar un
 mensaje de error y no contar ese numero como parte de los 5 numeros a ingresar.
 esto con el ciclo for '''
 