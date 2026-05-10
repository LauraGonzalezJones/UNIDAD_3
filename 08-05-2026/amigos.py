'''Desarrrolle una funcion que  reciba  2 numeros

como argumento y que me retorne un true o un false si son

 amigos




'''


def comprobar(n):
    suma = 0 # enpieza en 0
    for i in range (1,n):
        if n % i == 0:# pregunta si la division es exacta
            suma = suma + i #si es divisor
    return suma#revisa 
#funcion decide si dos numeros cumplen con ser amigos 
#
def son_amigos (num1, num2):
    resultado_1 = comprobar (num1)
    resultado_2 = comprobar (num2)

    if resultado_1 == num2 and resultado_2 == num1:
     return True
    else:
        return False
   # mas visual  con el ux 
num1 = int (input( "Ingresa el primer numero  "))
num2 = int(input ("Ingresa el segundo numero "))
print(son_amigos(num1,num2))
'''if son_amigos (num1, num2):
    print(f"El {num1} y el {num2} son amigos!")
else:
    print(f"El {num1} y el {num2} No son amigos")'''