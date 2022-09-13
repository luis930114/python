# -*- coding: utf-8 -*-
#
# Reto #1 - Multiplicar decimales
#Pide a tu usuario que ingrese 2 números con decimales (cuantos más mejor) y
# muestra el resultado de multiplicarlos ¿fácil, no?
#### Reto #2 - Reducir los decimales
#Toma como base el reto anterior,
#pero ajústalo para que el resultado muestre solamente 1, 2, 3 o 4 decimales.

def reto_2(numero_uno, numero_dos):
    decimales = int(raw_input("Ingresa el numero de decimales: "))
    resultado = round(numero_uno*numero_dos, decimales)
    return resultado

if __name__ == '__main__':
    numero_uno = float(raw_input("Ingresa el numero uno: "))
    numero_dos = float(raw_input("Ingresa el numero dos: "))

    print(reto_2(numero_uno,numero_dos))

    '''print(numero_uno * numero_dos)  reto numero uno '''
