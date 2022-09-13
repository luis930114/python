# -*- coding: utf-8 -*-
#Reto #1 “Hola Mundo”
#Instrucciones: este es un clásico de clásicos, pero haremos un pequeño cambio.
# En lugar de solo imprimir un mensaje en pantalla,
# pedirás al usuario que digite un nombre y mostrarás en pantalla lo siguiente: Hola, [nombre]
#
if __name__ == '__main__':
    hola = str(raw_input('escriba el nombre: '))
    print "hola, {}".format(hola)
#terminado
#
#Reto #2 “Hola… nombre y apellido:”
#Instrucciones: Ahora que sabemos incluir nombres, podemos agregar más datos.
#Intentemos con un apellido para tener algo así: ``Hola, [nombre] [apellido]```
