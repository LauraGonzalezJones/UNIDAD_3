#       0 1 2 3 4 5 6 7 8 9
a = [ 8,4,10,6,9,3,1,5,7,13 ]
# 1. Definimos la lista de números con los que vamos a trabajar


# 2. Iniciamos un ciclo que se repetirá desde la posición 0 hasta la 8
# x es el "puntero" que nos dice en qué posición estamos parados
for x in range(0, 9, 1): 

    # 3. Comparamos: ¿Es el número actual (a[x]) mayor que el de su derecha (a[x+1])?
    if a[x] > a[x + 1]: 
        
        # --- Si la respuesta es SÍ, hacemos el intercambio (swap) ---
        
        # 4. Guardamos el valor de la izquierda en una "caja temporal" (aux)
        # Esto se hace para no perder el número al sobreescribirlo
        aux = a[x]
        
        # 5. Movemos el número de la derecha hacia la posición de la izquierda
        a[x] = a[x + 1]
        
        # 6. Ponemos el número que guardamos en la "caja temporal" en la derecha
        a[x + 1] = aux