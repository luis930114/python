# -*- coding: utf-8 -*-
# Reto #10 “Conversor de millas”
#Instrucciones: hay 1.609344 km en una milla (mi).
#Escribe un programa en el que el usuario indique una cantidad de millas y
#muestre en pantalla el resultado convertido a kilómetros.
#
# 1 mill => 1.61
# millas => X

if __name__ == '__main__':
    Milla_ = float(1.609344)
    millas = float(raw_input("digite el numero de millas: "))
    total =  millas * Milla_
    print('las millas {}  en kilómetros vale {} km'.format(millas,total))
