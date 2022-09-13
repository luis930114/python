# -*- coding: utf-8 -*-
#Reto #5 “Suma y multiplicación”
#Instrucciones: añadiendo un extra al reto anterior ahora el usuario ingresará 3 números,
#sumarás los 2 primeros y el resultado será multiplicado por el tercero.
#Añade las consideraciones del punto decimal del reto anterior.
#Ejemplo:
#Datos de entrada:2, 3, 4
#Resultado:20


if __name__ =='__main__':
    numero_1 = float(raw_input("escriba el primero numero puede ser con decimales: "))
    numero_2 = float(raw_input("escriba el segundo numero: "))
    numero_3 = float(raw_input("escriba el tercer numero: "))
    suma = numero_1 + numero_2
    resultado = suma * numero_3
    print(resultado)
