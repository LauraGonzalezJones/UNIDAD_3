''' indice que va de 0 a 3
'''
a =[ 8,3,1,7]
aux = a [2] # el valor de indice 2 es 1, entonces aux es igual a 1
a[2] = a[0 ] # el valor del indice 0 es 8, entonces el indice 2 ahora es igual a 8
a[0] = aux # el valor de aux es 1, entonces el indice 0 ahora es igual a 1
# print(a) # seria [1,3,8,7]
print(a)