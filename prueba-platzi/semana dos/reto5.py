# -*- coding: utf-8 -*-
#
# Reto #5 - ¿Cómo está el clima?
#Crea un programa que pregunte al usuario si está lloviendo,
#en caso de responder “sí” pregunta si está haciendo mucho viento y
#si responde “sí” nuevamente muestra un mensaje indicando que hace mucho viento
#para salir con una sombrilla.
#En caso contrario, anima al usuario a que lleve una sombrilla.
#Para el caso de responder “no” en la primer pregunta, entonces solo desea un bonito día.
#Considera que las respuestas pueden pasarse a minúsculas para evitar posibles errores.

if __name__ == '__main__':
    clima_1 = str(raw_input("¿Esta lloviendo?"))
    if clima_1.lower() == 'si':
        clima_2 = str(raw_input("¿Esta haciendo mucho viento?"))
        if clima_2.lower() == 'si':
            print('Hace mucho viento para salir con una sombrilla')
        else:
            print('Animate a salir pero con una sombrilla')
    else:
        print('Ten un lindo dia :)')
