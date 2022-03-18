def contador_substrings():
    string = input('Ingrese una string: ')
    substring = input('Ingrese la substring a contar: ')
    contador = 0

    for letra in string:
        if letra == substring:
            contador += 1
    print (int(contador))

contador_substrings()
