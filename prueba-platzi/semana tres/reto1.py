# -*- coding: utf-8 -*-
#
# Reto #1 Longitud del string
#Pide a tu usuario que ingrese el nombre de su curso favorito,
#obtén la longitud de ese string y muéstralo en pantalla.
#

if __name__ == '__main__':
    curso_favorito = str(raw_input("ingrese su curso favorito: "))
    print('la longitud de la palabra es : {}'.format(len(curso_favorito)))
