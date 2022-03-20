def ubbi_dubbi(traduccion):
    vocales =  ['a', 'e', 'i', 'o', 'u']
    palabra_nueva = ''

    for vocal in traduccion:
        if vocal in vocales:    # o "if vocal in  'aeiou': "  
            vocal = 'ub' + vocal
        else:
            vocal = vocal
        palabra_nueva = palabra_nueva + vocal    
    print (palabra_nueva)



palabra = input('Ingrese una palabra: ')
ubbi_dubbi(palabra)
