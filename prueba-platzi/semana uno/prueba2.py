# -*- coding: utf-8 -*-
# #Reto #2 “Hola… nombre y apellido:”
#Instrucciones: Ahora que sabemos incluir nombres, podemos agregar más datos.
#Intentemos con un apellido para tener algo así: ``Hola, [nombre] [apellido]```
if __name__ == '__main__':
    nombre = str(raw_input('escriba el nombre: '))
    apellido = str(raw_input('escriba el apellido: '))
    print "hola, {} {}".format(nombre,apellido)
#terminado
