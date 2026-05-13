import time # Importamos la librería para controlar el tiempo

x = 0
# CICLO EXTERNO: Controla las HORAS (de 0 a 23)
while x <= 23:
    y = 0
    # CICLO MEDIO: Controla los MINUTOS (de 0 a 59)
    # Por cada hora que pasa, este ciclo se repite 60 veces
    while y <= 59:
        z = 0
        # CICLO INTERNO: Controla los SEGUNDOS (de 0 a 59)
        # Este es el que se mueve más rápido
        while z <= 59:
            # Imprime el formato de hora actual x:y:z
            print(x, ":", y, ":", z)
            
            # Pausa la ejecución por 0.1 segundos para que sea legible
            time.sleep(0.1) 
            
            # Incrementa los segundos
            z = z + 1 
            
        # Cuando Z llega a 60, sale del ciclo interno e incrementa un MINUTO
        y = y + 1 
        
    # Cuando Y llega a 60, sale del ciclo medio e incrementa una HORA
    x = x + 1 

print("Fin") # Solo se ejecuta cuando pasan las 24 horas completas