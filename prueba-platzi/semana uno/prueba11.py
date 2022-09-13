# -*- coding: utf-8 -*-
# Reto #11 “Cuantas veces un número en otro”
#Instrucciones:
#pide al usuario ingresar un número mayor a 1000 y otro menor a 100.
#Indica de una forma sencilla de entender al usuario
#cuantas veces cabe el número menor a 100 en el número mayor a 1000

if __name__ == '__main__':
    numero_1 = int(raw_input("ingrese un numero mayor a 1000: "))
    numero_2 = int(raw_input("ingrese un numero menor a 100: "))
    total = numero_1 / numero_2
    print('el numero {} cabe en el numero {} :  {} veces'.format(numero_2, numero_1, total))
