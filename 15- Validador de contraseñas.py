# PRIMERA DEPURACION
"""
- Poseer una longitud mínima de 6 caracteres.

- Contar con por lo menos una letra en Mayúsculas.
- Contar con por lo menos una vocal en Mayúsculas.

- Contar con por lo menos tres dígitos.
    - Los dígitos no deben ser consecutivos. Por ejemplo 123 o 456 no son combinaciones válidas. Por el contrario 168 y 414 si lo so
- Poseer por lo menos con un carácter espacial (?*%&@)
- Las contraseñas no pueden comenzar con la palabra _Password_.
"""

def is_valid_vocales(password):
    for caracter in password:
        if caracter in 'AEIOU':
            return True
    
    return False

    
def is_valid_letras(password):
    for caracter in password:
        if caracter in 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ':
            return True
    
    return False


def is_valid_numeros(password):
    contador = 0
    
    for caracter in password:
        if caracter in '1234567890':
            contador += 1
    
    if contador < 3:
        return False
    else:
        return True


def is_valid_especiales(password):
    for caracter in password:
        if caracter in '?*%&@':
            return True
    
    return False

def is_valid_password(password):
    
    if len(password) < 6:
        return False
    
    if is_valid_vocales(password) == False:
        return False
    
    if is_valid_letras(password) == False:
        return False
    
    if is_valid_numeros(password) == False:
        return False
    
    if is_valid_especiales(password) == False:
        return False
    
    if password[0:8] == 'password':
        return False
    
    return True


resultado = is_valid_password('PAssword152?')
print(resultado)
