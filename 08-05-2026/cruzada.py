'''
Desarrolle una función que reciba dos listas y
 retorne una lista con la suma cruzada.


'''
def cruzada (lista_1, lista_2): 
    # Creamos una lista vacía para almacenar los resultados de las sumas
    resultado = []

    # Suma el elemento en el índice 3 de lista_1 (el cuarto) 
    # con el índice 0 de lista_2 (el primero)
    suma1 = lista_1[3] + lista_2[0] 
    resultado.append(suma1)

    # Suma el índice 2 de lista_1 con el índice 1 de lista_2
    suma2 = lista_1[2] + lista_2 [1]
    resultado.append(suma2)

    # Suma el índice 1 de lista_1 con el índice 2 de lista_2
    suma3 = lista_1[1] + lista_2 [2]
    resultado.append (suma3)

    # Suma el índice 0 de lista_1 con el índice 3 de lista_2
    suma4 = lista_1 [0] + lista_2[3]
    resultado.append (suma4)

    # Devuelve la lista 'resultado' con las 4 sumas realizadas
    return resultado

# Definición de las listas de entrada
lista_1  = [3, 1, 8, 6]
lista_2 = [ 9, 4, 6, 5]

# Llamada a la función e impresión del resultado final
print(cruzada(lista_1, lista_2))
