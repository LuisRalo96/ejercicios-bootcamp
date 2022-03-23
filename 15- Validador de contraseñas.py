#Hecho por el profe
"""
- Poseer una longitud mínima de 6 caracteres.

- Contar con por lo menos una letra en Mayúsculas.
- Contar con por lo menos una vocal en Mayúsculas.

- Contar con por lo menos tres dígitos.
    - Los dígitos no deben ser consecutivos. Por ejemplo 123 o 456 no son combinaciones válidas. Por el contrario 168 y 414 si lo so
- Poseer por lo menos con un carácter espacial (?*%&@)
- Las contraseñas no pueden comenzar con la palabra _Password_.
"""

def is_valid_password(password):
    
    if len(password) < 6:
        return False
    
    contador = 0
    
    letras = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    vocales = 'AEIOU'
    numeros = '1234567890'
    especiales = '?*%&@'
    
    condicion_dos = False
    condicion_tres = False
    condicion_cuatro = False
    condicion_cinco = False
    
    for caracter in password:
        
        if caracter in letras: # Si existe una letra en Mayúscula la condición se cumple.
            condicion_dos = True
            
        if caracter in vocales: # Si existe una vocal en Mayúscula la condición se cumple.
            condicion_tres = True
    
        if caracter in numeros:
            contador += 1
            
        if caracter in especiales:
            condicion_cinco = True

    if condicion_dos == False:
        return False
    
    if condicion_tres == False:
        return False
    
    if contador < 3:
        return False
    
    if condicion_cinco == False:
        return False

    #[pos inicial:pos final] Donde pos final = pos final - 1
    if password[0:8] == 'password':
        return False
    
    return True


resultado = is_valid_password('PAssword152?')
print(resultado)
