#cifrado de letra#

array="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
clave=("A,23")

def alfabeto(clave,C):

    idx = array.index(C) 
    letracif=array[(idx+clave%len(array))]
    return letracif

#-----------------------------------------------------#

#Cifrado de mensaje#

array = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def alfabeto(clave, C):
    idx = array.index(C)
    letracif = array[(idx + clave) % len(array)]
    return letracif

def cifrar_mensaje(clave, mensaje):
    mensaje_cifrado = ""
    for letra in mensaje:
        if letra in array:
            mensaje_cifrado += alfabeto(clave, letra)
        else:
            mensaje_cifrado += letra  # Si la letra no está en el alfabeto, se añade tal cual
    return mensaje_cifrado

mensaje = "ENELCIELOAZULDEUNDIACLAROBAILANLOSSUEÑOSLIBRESYRAROSCONELVIENTOSUSURRANSECRETOSENCADARINCONNUEVOSRETOS"
clave = 23

#-----------------------------------------------------#

#descifrado de mensaje#

array = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
clave = 23
mensaje = "ENELCIELOAZULDEUNDIACLAROBAILANLOSSUEÑOSLIBRESYRAROSCONELVIENTOSUSURRANSECRETOSENCADARINCONNUEVOSRETOS"

def descifrar(clave, mensaje):
    array = "mensaje"
    s = ""
    for i in mensaje:
        if i in array:
            idx = array.index(i)
            frasecif = array[(idx - clave) % len(array)]
            s += frasecif
        else:
            s += i
    return s

#-----------------------------------------------------#

#cifrado de mensaje hola#

array = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
clave = 3
palabra = "HOLA"

def alfabeto(clave, letra):
    posicion = array.index(letra)
    return array[(posicion + clave) % len(array)]

def cifrar_palabra(clave, mensaje):
    palabra_cifrada = ""
    for letra in mensaje:
        if letra in array:
            palabra_cifrada += alfabeto(clave, letra)
        else:
            palabra_cifrada += letra  
    return palabra_cifrada

#-----------------------------------------------------#

#descifrado de mensaje cde#

array = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
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

#Cifrado de mensaje ¡Hola Mundo!#

array = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
clave = 3
mensaje = "¡HOLA MUNDO!"

def alfabeto(clave, letra):
    posicion = array.index(letra)
    return array[(posicion + clave) % len(array)]

def cifrar_palabra(clave, mensaje):
    palabra_cifrada = ""
    for letra in mensaje:
        if letra.upper() in array:
            if letra.isupper():
                palabra_cifrada += alfabeto(clave, letra.upper())
            else:
                palabra_cifrada += alfabeto(clave, letra.upper()).lower()
        else:
            palabra_cifrada += letra  
    return palabra_cifrada

#-----------------------------------------------------#

#cifrado de letra#
#alfabeto(3,"A")
#print(alfabeto(3,"A"))

#Cifrado del mensaje
#mensaje_cifrado = cifrar_mensaje(clave, mensaje)
#print(mensaje_cifrado)

#Descifrado del mensaje
#mensaje_descifrado = descifrar(clave, mensaje)
#print(mensaje_descifrado)

#Cifrado de mensaje hola
#palabra_cifrada = cifrar_palabra(clave, palabra)
#print(palabra_cifrada)

#descifrado de mensaje cde
#mensaje_descifrado = descifrar_mensaje(clave, mensaje)
#print(mensaje_descifrado)

#Cifrado de mensaje ¡Hola Mundo!
#cifrar_palabra = cifrar_palabra(clave, mensaje)
#print(cifrar_palabra)