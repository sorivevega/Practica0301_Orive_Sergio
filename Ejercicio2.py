#Escribir una función que lea dos ficheros csv con una lista larga de datos de personas (50 personas y 1000 personas) y llame a dos funciones que pongan su nombre en formato capitalizado y calculen la letra de DNI correspondiente. Realiza la comprobación de rendimiento con la librería cProfile y muestra los datos. Describe que indica cada dato que nos proporciona cProfile.

import cProfile
def Mayusculas(x):
    for i in x:
        name = i.title()
        print (name)
    
    '''
    Este codigo lo que hace es coger las cadenas y poner la primera letra de la cadena en mayuscula y la imprime
    El parametro de entrada es el archivo .csv que elegimos mas adelante
    '''
def Letras(x):
    letras={0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q", 17:"V",18:"H", 19:"L", 20:"C",21:"K",22:"E"}
    for i in x:
        y=i.split(",")
        num = y[1].strip()
        num = int(num) 
        letra_dni = letras[num % 23]
        print("DNI: ",y[1], "Letra: ",letra_dni)
    
    '''
    Esta funcion primero lee todos los nombres del documento .csv
    Lo que hace esta funcion es primero ver el diccionario con las letras y el numero asignado.
    Separa las letras por las comas
    despues suma todas las letras que se encuentran en el documento .csv y lo divide entre 23 para obtener el numero y con ello, la letra del DNI en cuestion
    El parametro de entrada es el archivo .csv que elegimos mas adelante
    '''
    
def procesar_fichero():
    r = input("Dime un fichero: 50.csv o 1000.csv ")
    
    with open(r, 'r') as file:
        lista = file.readlines()
    Mayusculas(lista)
    Letras(lista)  

    '''
    Esta funcion lo que hace es preguntar que archivo quieres que lea
    Una vez lo sabe, lo abre y lo lee.
    Una vez esta abierto y lo lee, aplica las funciones anteriores sobre la lista que le hemos dicho que lea que es el archivo ,csv
    '''
cProfile.run('procesar_fichero()')

