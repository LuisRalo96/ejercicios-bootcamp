def pares(lista):
    cantidad_elemento = len(lista) / 2
    numeros_pares = 0

    for elemento in lista:
        if elemento % 2 == 0:
            numeros_pares += 1

    if numeros_pares > cantidad_elemento:
        print ('True')
    else:
        print ('False')


rango_lista = int(input('¿Qué cantidad de números ingresaras?: '))

numeros = []

for numero in range(rango_lista):
    numeros.append(int(input("Inserta número: ")))

pares(numeros)
