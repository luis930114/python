# -*- coding: utf-8 -*-

#Reto #6 - Edad permitida
#Pide al usuario que ingrese su edad y mostrarás un mensaje correspondiente si
#esta coincide con las siguientes condiciones:
#Más de 30 años: Nunca es tarde para aprender ¿Qué curso tomaremos?
#Entre 29 y 18 años: Es un momento excelente para impulsar tu carrera.
#Menos de 18 años: ¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.

if __name__ == '__main__':
    edad = int(raw_input('ingresa tu edad: '))

    if edad >= 30:
        print('Nunca es tarde para aprender ¿Qué curso tomaremos?')
    if (edad >= 18) and (edad <= 29):
        print('Es un momento excelente para impulsar tu carrera.')
    if edad < 18:
        print('¿Sabes hacia dónde dirigir tu futuro? Seguro puedo ayudarte.')
