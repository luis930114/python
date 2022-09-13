# -*- coding: utf-8 -*-
#
# Reto #7 ¡Hablemos Pig Latin! (Puerco Latino) 🐷
#Solo una cosa, pide a tu usuario que ingrese una palabra y tradúcela a Pig Latin.

#Espera ¡¿qué?!
#PuercoLatino es como el idioma de la “efe”,
#donde cambiamos las palabras bajo ciertas condiciones. En este caso será así:

#La primer consonante de una palabra se pasa al final y se agrega la sílaba “ay”.
#Si una palabra inicia con vocal, se agrega “way” al final.
#Ejemplos:

#Platzi 👉 Latzipay
#Abeja 👉 Abejaway
#A
list_vocales = ['a','e','i','o','u']
list_consonantes = ['b','c','d','f','g','h','j','k','l','m','ñ','n','p','q','r','s',
                't','v','w','x','y','z']


def obtener_nueva_palabra(palabra):
    primer_letra = palabra[0].lower()
    letra_nueva = ""
    if primer_letra in list_consonantes:
        letra_nueva = palabra[1: len(palabra)] + primer_letra + "ay"
    if primer_letra in list_vocales:
        letra_nueva = palabra + "way"
    return letra_nueva

if __name__ == '__main__':
    palabra = str(raw_input("Ingrese una palabra: "))
    result = obtener_nueva_palabra(palabra)
    print(result)
