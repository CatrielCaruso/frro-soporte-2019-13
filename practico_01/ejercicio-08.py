'''Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
Escribir la función usando el bucle for anidado.'''


def superposicion(a,b):
 cont=0

 for i in range(0,len(a)):

  for j in range(0,len(b)):

    if(a[i]==b[j]):
       cont = cont + 1

 if (cont > 0):
     return True

 else:

     return False




pass

assert superposicion([1,2,3,4],[1,5,6,7])==True
assert superposicion([1,2,3,4],[5,6,7,8])==False