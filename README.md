# ejercicios-bootcamp
ejercicios prof Eduardo

2.-Reemplazar vocales por posiciones

Dado un string de longitud N. Donde N es mayor a 0.

Ejemplo.

'Hola mundo'

Desarrolla un programa en Python que permite reemplazar todas las vocales del String por sus correspondiente posición en la lista.

Donde las posiciones serán las siguientes.

a = 1

e = 2

i = 3

o = 4

u = 5

Salida.

'H4l1 m5nd4'


5.- Contador de substrings.

Desarrolla una función que permita conocer la cantidad de veces que existe un substring en un string.

La función debe cumplir con los siguientes requerimientos.

La función debe tener por nombre _contador*substrings*.
La función debe recibir como argumento el string a evaluar y el substring del cual se quiere conocer la cantidad de coincidencias.
La función debe retornar, mediante un número entero, la cantidad de veces que existe el substring en el string original.
Ejemplos.

-> contador_substrings('Hola mundo', 'o')
2

-> contador_substrings('Nuevo ejercicio en PyWombat', 'ue')
1

-> contador_substrings('Contador de caracteres', 'de')
1

-> contador_substrings('PyWombat Ejercicios de Python con extensión Py', 'Py')
3

Restricción: No es posible utilizar el método count del String. 


6.- Cantidad de dígitos número entero.

Definir una función la cual nos permita conocer cuántos dígitos posee un número.

* La función debe tener por nombre cantidad_digitos.
* La función debe poseer el parámetro numero.
* La función debe retornar la cantidad de dígitos del parámetro.
* No es posible utilizar la función str.

Ejemplos

-> cantitdad_digitos(10)
2

-> cantitdad_digitos(2019)
4

-> cantitdad_digitos(1234567890)
10
