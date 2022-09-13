# -*- coding: utf-8 -*-
#
# Reto #2 ‘Suma’ de strings
#Crea un programa en el que le pidas en 3 variables distintas: nombre, apellido y comida favorita.
# Como salida mostrarás el mensaje Hola, mi nombres es {nombre} {apellido} y
#  mi comida favorita es {comida} en un solo string.
#
if __name__ == '__main__':
    nombre = str(raw_input("Escribe tu nombre : "))
    apellido = str(raw_input("Escribe tu apellido : "))
    comida_favorita = str(raw_input("Escribe tu comida favorita : "))
    print(''' Hola, mi nombres es {} {} y mi comida favorita es {}'''.format(nombre, apellido, comida_favorita))
