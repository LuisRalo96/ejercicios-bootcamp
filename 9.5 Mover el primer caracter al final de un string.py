string = input('Inserte palabra: ')
string_list = list(string)
primera_parte = ''.join(string_list[1:])
ultima_letra = string_list[0]
nueva_palabra = primera_parte + ultima_letra

print (primera_parte + ultima_letra)
