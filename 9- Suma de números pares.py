def suma_pares(lista):
    suma = 0

    for elemento in lista:
        if elemento % 2 == 0:
            suma += elemento

    print (suma)


rango_lista = int(input('¿Qué cantidad de números ingresaras?: '))

numeros = []

for numero in range(rango_lista):
    numeros.append(int(input("Inserta número: ")))

suma_pares(numeros)
