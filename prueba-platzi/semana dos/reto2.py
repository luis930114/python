# -*- coding: utf-8 -*-

#Reto #2 - En el rango, por favor.
#Pide al usuario que indique 2 números: uno que servirá como límite y otro para comparar.
#Si el segundo número es menor al primero,
#mostrarás un mensaje diciendo
#“El número ‘x’ se encuentra en el rango, gracias” y en caso contrario dirá “El número ‘x’
#excede el límite permitido”.

def comparar_limite(limite, indice):
    if indice < limite:
        print('el numero {} se encuentra en el rango, gracias'.format(indice))
    else:
        print('el numero {} excede el limite permitido'.format(indice))

if __name__ == '__main__':
    numero_1 = int(raw_input("ingrese el numero uno: "))
    numero_2 = int(raw_input("ingrese el numero dos: "))

    comparar_limite(numero_1, numero_2)
