#Parte mio, corregido con el profe
def contador_substrings(string, substring):
    contador = 0 #Local

    cantidad = len(string)
    cantidad_substring = len(substring)
    for pos_inicial in range(0,cantidad):
        posicion_final = pos_inicial + cantidad_substring
        #string [pos_inicial:pos_final]
        caracteres = string[pos_inicial: posicion_final]
        #print (caracteres)

        if caracteres == substring:
            contador += 1

    return contador


string = input('Ingrese una string: ')
substring = input('Ingrese la substring a contar: ')

resultado = contador_substrings(string, substring)
print(resultado )
