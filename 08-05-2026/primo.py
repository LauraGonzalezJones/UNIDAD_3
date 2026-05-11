'''# El usuario ingresa un número
num = int(input("Ing. número :"))

# Contador de divisiones exactas
divisibles = 0

# Recorre desde 1 hasta el número ingresado
for x in range(1, num + 1):

   # Verifica si la división es exacta
   if num % x == 0:

      # Suma 1 al contador
      divisibles = divisibles + 1

# Si tiene exactamente 2 divisores
if divisibles == 2:

   # El número es primo
   print("Primo")

else:

v   # El número no es primo
   print("No es primo")

'''

def es_primo(numero):
   divisibles = 0

   for x in range(1, numero + 1):
      if numero % x == 0:
         divisibles = divisibles + 1

   if divisibles == 2:
      return True
   else:
      return False

n = int (input("ing.numero:"))
if es_primo (n):
   print("primo")
else:
   print("no es primo") 



    
# contar primos 
def los_primeros_numeros_primos(cuantos):
   contar_primo = 1
   n = 1
   while contar_primo <= cuantos:
      if es_primo(n):
         print(f"{contar_primo} -> {n} es primo")
         contar_primo = contar_primo + 1

      n = n + 1
los_primeros_numeros_primos(50)