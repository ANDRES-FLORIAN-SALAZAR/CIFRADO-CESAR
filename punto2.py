# Cifrado de palabra 

#array = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#clave = 3
#mensaje = "HOLA"

#def alfabeto(clave, letra):
#    posicion = array.index(letra)
#    return array[(posicion + clave) % len(array)]

#def cifrar_palabra(mensaje, clave):
#    palabra_cifrada = ""
#    for letra in mensaje:
#        if letra in array:
#            palabra_cifrada += alfabeto(clave, letra)
#        else:
#            palabra_cifrada += letra  
#    return palabra_cifrada

#-----------------------------------------------------#

#Descifrado de mensaje#

array = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
clave = 5
mensaje = "CDE"

def alfabeto_descifrar(clave, letra):
    posicion = array.index(letra)
    return array[(posicion - clave) % len(array)]

def descifrar_mensaje(clave, mensaje):
    mensaje_descifrado = ""
    for letra in mensaje:
        if letra in array:
            mensaje_descifrado += alfabeto_descifrar(clave, letra)
        else:
            mensaje_descifrado += letra  
    return mensaje_descifrado

#-----------------------------------------------------#

#cifrado de mensaje ¡HOLA MUNDO!#

#array = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#mensaje = "¡HOLA MUNDO!"
#clave = 3

#def alfabeto(clave, letra):
#    posicion = array.index(letra)
#    return array[(posicion + clave) % len(array)]

#def cifrar_palabra(mensaje):
#    palabra_cifrada = ""
#    for letra in mensaje:
#        if letra in array:
#            palabra_cifrada += alfabeto(clave, letra)
#        else:
#            palabra_cifrada += letra  
#    return palabra_cifrada

#-----------------------------------------------------#

# Cifrado de palabra intercalada

array = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
clave = 3
mensaje = "¡HOLA MUNDO!"

def alfabeto(clave, letra):
    posicion = array.index(letra)
    return array[(posicion + clave * 2) % len(array)]

def cifrar_palabra(clave, mensaje):
    palabra_cifrada = ""
    for letra in mensaje:
        if letra.upper() in array.upper():
            letra_array = array[array.upper().index(letra.upper())]
            if letra.isupper():
                palabra_cifrada += alfabeto(clave, letra_array).upper()
            else:
                palabra_cifrada += alfabeto(clave, letra_array).lower()
        else:
            palabra_cifrada += letra  
    return palabra_cifrada

#-----------------------------------------------------#

# Descifrado del mensaje intercalado

#array = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
#clave = 5
#mensaje = "CDE"

#def alfabeto_descifrar(clave, letra):
#    posicion = array.index(letra)
#    return array[(posicion - clave * 2) % len(array)]

#def descifrar_mensaje(clave, mensaje):
#    mensaje_descifrado = ""
#    for letra in mensaje:
#        if letra in array:
#            mensaje_descifrado += alfabeto_descifrar(clave, letra)
#        else:
#            mensaje_descifrado += letra  
#    return mensaje_descifrado

#-----------------------------------------------------#

# Cifrado de mensaje ¡HOLA MUNDO! intercalado

#array = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
#clave = 3
#mensaje = "¡HOLA MUNDO!"

#def alfabeto(clave, letra):
#    posicion = array.index(letra)
#    return array[(posicion + clave * 2) % len(array)]

#def cifrar_palabra(mensaje):
#    palabra_cifrada = ""
#    for letra in mensaje:
#        if letra in array:
#            palabra_cifrada += alfabeto(clave, letra)
#        else:
#            palabra_cifrada += letra  
#    return palabra_cifrada

#-----------------------------------------------------#

# Cifrar palabra y simbolos

#array = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!@#$%^&*()_+-=[]{}|;:'\",.<>?/~`"
#clave = 3
#mensaje = "HOLA"

#def alfabeto(clave, letra):
#    posicion = array.index(letra)
#    return array[(posicion + clave*2) % len(array)]

#def cifrar_palabra(mensaje, clave):
#    palabra_cifrada = ""
#    for letra in mensaje:
#        if letra in array:
#            palabra_cifrada += alfabeto(clave, letra)
#        else:
#            palabra_cifrada += letra  
#    return palabra_cifrada

#-----------------------------------------------------#

# Descifrar el mensaje y simbolos

array = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!@#$%^&*()_+-=[]{}|;:'\",.<>?/~`"
clave = 5
mensaje = "CDE"

def alfabeto_descifrar(clave, letra):
    posicion = array.index(letra)
    return array[(posicion - clave) % len(array)]

def descifrar_mensaje(clave, mensaje):
    mensaje_descifrado = ""
    for letra in mensaje:
        if letra in array:
            mensaje_descifrado += alfabeto_descifrar(clave, letra)
        else:
            mensaje_descifrado += letra  
    return mensaje_descifrado

#-----------------------------------------------------#

# Cifrar el mensaje y simbolos

array = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz!@#$%^&*()_+-=[]{}|;:'\",.<>?/~`"
mensaje = "¡HOLA MUNDO!"
clave = 3

def alfabeto(clave, letra):
    posicion = array.index(letra)
    return array[(posicion + clave*2) % len(array)]

def cifrar_palabra(mensaje):
    palabra_cifrada = ""
    for letra in mensaje:
        if letra in array:
            palabra_cifrada += alfabeto(clave, letra)
        else:
            palabra_cifrada += letra  
    return palabra_cifrada

#-----------------------------------------------------#

# Cifrado de palabra
#mensaje_cifrado = cifrar_palabra(mensaje, clave)
#print(mensaje_cifrado)

# Descifrado del mensaje
#mensaje_descifrado = descifrar_mensaje(clave, mensaje)
#print(mensaje_descifrado)

# Cifrado de mensaje ¡HOLA MUNDO!
#cifrado = cifrar_palabra(clave, mensaje)
#print(cifrado)

# Cifrado de palabra intercalada
#cifrado = cifrar_palabra(clave, palabra)
#print(cifrado)

# Descifrado del mensaje intercalado
#mensaje_descifrado = descifrar_mensaje(clave, mensaje)
#print(mensaje_descifrado)

# Cifrado de mensaje ¡HOLA MUNDO! intercalado
#cifrar_palabra = cifrar_palabra (mensaje)
#print(cifrar_palabra)

# Cifrar palabra y simbolos
#cifrado = cifrar_palabra(mensaje, clave)
#print(cifrado)

# Descifrar el mensaje y simbolos
#mensaje_descifrado = descifrar_mensaje(clave, mensaje)
#print(mensaje_descifrado)

# Cifrar el mensaje y simbolos
#cifrado = cifrar_palabra(mensaje)
#print(cifrado)