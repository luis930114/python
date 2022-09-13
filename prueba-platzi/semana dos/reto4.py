# -*- coding: utf-8 -*-
#
# Reto #4 - “I like turtles”
#Escribe un programa que pida al usuario ingrese su animal favorito,
#si coloca ‘Tortuga’, ‘tortuga’, ‘TORTUGA’ o cualquier otra variante de la palabra
#entonces mostrar en pantalla “También me gustan las tortugas”.
#En caso contrario mostrar el mensaje “Ese animal es genial, pero prefiero las tortugas”.

if __name__ == '__main__':
    animal = str(raw_input("ingresa tu animal favorito: "))

    if animal.lower() == "tortuga":
        print('También me gustan las tortugas')
    else:
        print('Ese animal es genial, pero prefiero las tortugas')
