# -*- coding: utf-8 -*-
# Reto #9 “Calculando días”
#Instrucciones: escribe un programa al que le indiques una cantidad de días y
#como resultado deberá mostrar cuantas horas,
#minutos y segundos hay en dicha cantidad de días


if __name__ == '__main__':
    num_dias = int(raw_input("numero de dias : "))
    horas = num_dias * 24
    minutos = horas * 60
    segundos = minutos * 60

    print('el numero de horas es {} el numero de minutos es {} y los segundos son {}'.
    format(horas,minutos,segundos))
