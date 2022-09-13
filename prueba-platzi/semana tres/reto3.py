# -*- coding: utf-8 -*-
#
# Reto #3 Ajusta las iniciales
#Ahora, pedirás a tu usuario que ingrese su nombre, apellido y país de origen en minúsculas.
#Después mostrarás los datos de salida con mayúscula inicial al tratarse de nombres propios.

if __name__ == '__main__':
    nombre = str(raw_input("Escribe tu nombre : "))
    apellido = str(raw_input("Escribe tu apellido : "))
    pais = str(raw_input("Escribe tu pais : "))
    print("nombre : {}-- apellido: {} -- pais: {}".format(nombre.capitalize(),
    apellido.capitalize(), pais))
