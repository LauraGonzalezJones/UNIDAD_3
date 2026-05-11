import time

x = 0
while x <= 23:
   y = 0
   while y <= 59:
      z = 0
      while z <= 59:
         print(x, ":", y, ":", z)
         time.sleep(0.1)
         z = z + 1
      y = y + 1
   x = x + 1
print("Fin")