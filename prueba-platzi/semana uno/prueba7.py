# -*- coding: utf-8 -*-
# Reto #7 “Edad futura y pasada”
#Instrucciones: pide al usuario que indique su nombre y su edad.
#Como mensaje de salida le indicarás que edad tuvo el año pasado y cuantos años tendrá el siguiente año.
#Ejemplo: [nombre] el año pasado tenías X años y el próximo año cumplirás Y años.

if __name__ == '__main__':
    nombre = str(raw_input("escribe tu nombre: "))
    edad = int(raw_input("escribe tu edad: "))
    anio_pasado = edad - 1
    anio_siguiente = edad + 1
    print('{} el año pasado tenias {} y el proximo año cumplirásas {} años'.
    format(nombre,anio_pasado,anio_siguiente))
