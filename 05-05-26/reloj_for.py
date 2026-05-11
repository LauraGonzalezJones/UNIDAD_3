# crear un reoj con for en terminal 
import time

while True:# el ciclo sera infinito 
    for h in range(0, 24,1): # el 0 es de donde parte el ciclo, el 24 es la condicion y el 1 es el incremento, entonces el ciclo se ejecutara mientras la variable h sea menor que 24, y en cada iteracion se incrementara en 1, entonces el ciclo se ejecutara 24 veces, ya que despues de la primera iteracion h sera igual a 1, y la condicion se cumplira hasta que h sea igual a 23, despues de eso el ciclo se detendra.

   
         for m in range(0, 60, 1): # el 0 es de donde parte el ciclo, el 60 es la condicion y el 1 es el incremento, entonces el ciclo se ejecutara mientras la variable m sea menor que 60, y en cada iteracion se incrementara en 1, entonces el ciclo se ejecutara 60 veces, ya que despues de la primera iteracion m sera igual a 1, y la condicion se cumplira hasta que m sea igual a 59, despues de eso el ciclo se detendra.
        
             for s in range(0, 60, 1):
         
                 print(h, ":", m, ":", s)
             time.sleep(0.01)
     
print("Fin")