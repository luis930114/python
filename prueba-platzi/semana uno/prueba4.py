# -*- coding: utf-8 -*-
# Reto #4 “Suma de enteros”
#Instrucciones: otro clásico conocido,
#donde pedirás al usuario que ingrese 2 números y muestre en pantalla el resultado.
#Si quieres añadir más dificultad puedes utilizar números con punto decimal y
#especificar el número de decimales después del punto.
#Ejemplo: 2.5633 + 5.6883 = 8.25

if __name__ == '__main__':
    numero_1 = float(raw_input("escriba el primero numero puede ser con decimales: "))
    numero_2 = float(raw_input("escriba el segundo numero: "))
    decimales = int(raw_input("escriba el total de decimales: "))
    suma = round(numero_1 + numero_2, decimales)
    print(suma)
