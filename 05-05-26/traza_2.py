# Inicializamos las horas en 0
x = 0
# CICLO EXTERNO: Controla las HORAS.
# Se ejecutará desde las 0 hasta las 23 (24 iteraciones).
while x <= 23:
    # Reiniciamos los minutos cada vez que cambia la hora.
    y = 0
    # CICLO MEDIO: Controla los MINUTOS.
    # Se repite 60 veces (de 0 a 59) por cada hora que pasa.
    while y <= 59:
        # Reiniciamos los segundos cada vez que cambia el minuto.
        z = 0
        # CICLO INTERNO: Controla los SEGUNDOS.
        # Es el que se mueve más rápido (de 0 a 59).
        while z <= 59:
            # Muestra la hora actual en formato H : M : S.
            print(x, ":", y, ":", z)
            # Incrementa el segundo actual.
            z = z + 1
        # Al terminar los 60 segundos, sumamos un minuto.
        y = y + 1
    # Al terminar los 60 minutos, sumamos una hora.
    x = x + 1

# Una vez que se completan las 24 horas, el programa termina.
print("FIN")