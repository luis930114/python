# -*- coding: utf-8 -*-
#Reto #4 String fragmentado
#Pongámonos más exigentes 💥
#Solicita a tu usuario que indique una oración de 10 o más caracteres,
#la línea de un poema o canción funcioona excelente.
#Calcula la longitud del string,
#pide un número de rango inicial y final que esté entre la longitud del string
#para al final mostrar el fragmento que incluya los caracteres en ese intervalo.
#
def obtener_fragmento_oracion(rango_inicial, rango_final, oracion, longitud):
    if (rango_inicial >= rango_final):
        return "el rango inicial sobrepasa el rango final"
    else:
        fragmento = oracion[rango_inicial: rango_final]
        return fragmento

if __name__ == '__main__':
    oracion = str(raw_input("Escribe una oracion de 10 o mas caracteres: "))
    rango_inicial = int(raw_input("Escribe un rango inicial: "))
    rango_final = int(raw_input("Escribe un rango final: "))
    longitud = len(oracion)
    fragmento = obtener_fragmento_oracion(rango_inicial, rango_final, oracion, longitud)
    print("{}".format(fragmento))
