# -*- coding: utf-8 -*-
import random


def run():
    number_found = False
    limite = int(raw_input('digite hasta que numero puede llegar: '))
    random_number = random.randint(0, limite)

    while not number_found:
        number = int(raw_input('Intenta un número：'))


        if number == random_number:
            print("Felicidades. Encontraste el número")
            number_found = True
        elif number > random_number:
            print('El número es más pequeño')
        else:
            print('El número es más grande')


if __name__ == '__main__':
    run()