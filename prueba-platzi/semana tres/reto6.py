# -*- coding: utf-8 -*-
#
#Reto #6 Nombres cortos y largos
#Ya sabemos trabajar con nombres ¿pero qué pasa si cumple ciertas cualidades?
#Tu usuario ingresará su nombre, si tiene una longitud mayor a 5 caracteres
#mostrarás un saludo con su nombre en pantalla.
#Si tiene menos de 5 caracteres, pedirás su apellido, mostrarás el saludo con nombre y apellido.
#En ambos casos deberás mostrarlos con mayúscula inicial.

if __name__ == '__main__':
    nombre = str(raw_input("Ingresa tu nombre : "))
    if len(nombre) > 5:
        print("hola, {}".format(nombre))
    else:
        apellido = str(raw_input("Ingresa tu apellido : "))
        print("hola, {} {}".format(nombre, apellido))
