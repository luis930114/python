# -*- coding: utf-8 -*-
#
# Reto #5 Mayúsculas y minúsculas
#Solicita a tu usuario que indique 2 palabras,
#donde al mostrarlas en pantalla una estará totalmente en mayúsculas y otra en minúsculas ¿fácil, no?
#

if __name__ == '__main__':
    palabra_uno = str(raw_input("escribe la primeroa palabra en mayuscula: "))
    palabra_dos = str(raw_input("escribe la primeroa palabra en minuscula: "))

    print("{} -- {}".format(palabra_uno.upper(), palabra_dos.lower()))
