#Escribir dos funciones, una función que reciba un número entero positivo n y calcule el número de fibonacci asociado a ese número de manera recursiva y otra función que haga la misma operación pero con bucles.
#Con ambas funciones, calcular y comparar el tiempo de ejecución para n = (1, 10, 20, 30 y 40) por fuerza bruta
import datetime


def Fibonacci_bucles(n):
    a, b = 0, 1
    for i in range (n):
        a, b = b, a + b
   
    return(a)
'''
Esta funcion lo que hace es calcular el numero de Fibonacci del numero n utilizando un bucle for.
Los primeros numeros para poder calcular cualquier numero de Fibonacci son el 0 y el 1 que es lo que encontramos
en la primera linea de codigo.
Despues con el comando 'for', recorre todos los nuemeros hasta que el que hemos metido y con la formula siguiente,
calcula el numero
Finalmente nos devuelve 'a'
Parametros de entrada: n
Parametro de salida: a
'''

st = datetime.datetime.now()    
print(Fibonacci_bucles(6))
et = datetime.datetime.now()
print(et-st)




def Fibonacci_recursiva(n):
    if n <= 1:
        return n
    else:
        return Fibonacci_recursiva(n-1) + Fibonacci_recursiva(n-2)

'''
Lo que hace esta funcion es calcular el numero de Fibonacci de un numero n utilizando recursion
Primero lo que hace es que si el numero que metemos es el numero 1 o 0 devuelve el numero metido ya que
el numero de Fibonacci de esos numeros son ellos mismos.
Si no es ninguno de esos numeros, lo que hace la funcion es devolver (n-1) + (n+2) que es la forma que se tiene de
calcular este numero de forma recursiva
'''
st = datetime.datetime.now()
print(Fibonacci_recursiva(40))
et = datetime.datetime.now()
print(et-st)