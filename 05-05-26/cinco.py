''' ejercicio desarrolle un programa que permita ingresar 5 numeros y 
al finalizar retorne cuantos numero pares ingreso el ux 
nota: solo deben considerar numeros positivos, el programa debe validar que el numero
 ingresado sea positivo, si el numero es negativo debe mostrar un
 mensaje de error y no contar ese numero como parte de los 5 numeros a ingresar.
 esto con el ciclo for '''
def contar_pares():
    contador_pares = 0
    intentos_validos = 0
    
    while intentos_validos < 5:
        # La función input siempre debe ir acompañada de int() para cálculos
        numero = int(input("Ingrese un número positivo: "))
        
        if numero >= 0:
            if numero % 2 == 0:
                contador_pares = contador_pares + 1
            # Esta línea es la que controla que solo se cuenten 5 números válidos
            intentos_validos = intentos_validos + 1 
        else:
            print("Error: El número debe ser positivo.")
            
    return contador_pares

# --- ESTA ES LA PARTE QUE FALTA ---
# Llamamos a la función y guardamos el resultado

print("La cantidad de números pares ingresados es:", contar_pares())