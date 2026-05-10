'''
 Desarrolle una función que retorne el factorial(factorial de 4 es 1*2*3*4) de un número.
 

'''

def calcular_factorial(n):
    if n < 0:
        return "No existe factorial de números negativos"
    
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i  # Multiplica el acumulado por el siguiente número
    return resultado
num = int(input("ingresa el numero del cual queres calcular el factorial "))

print(calcular_factorial(num)) # Salida: 120