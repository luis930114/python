# -*- coding: utf-8 -*-

# 6.	A un  trabajador le descuentan de su sueldo el 10% si es menor o igual a 1000,
# por encima de 1000 y hasta 2000 le descuentan el 3% del adicional, y por encima de 2000 el 5% del adicional.
# Calcular el  descuento y sueldo neto que recibe el trabajador dado su sueldo.

def obtener_descuento(sueldo):
    if sueldo <= 1000:
        return sueldo * 0.1
    if (sueldo > 1000) and (sueldo <= 2000):
        return sueldo * 0.03
    if sueldo > 2000:
        return sueldo * 0.05

def obtener_sueldo_neto(sueldo):
     return sueldo - obtener_descuento(sueldo)

def main():
    sueldo = float(input("Ingrese el sueldo base: "))
    print("""
        El sueldo neto del trabajador es de {} y su descuento es de {}
    """.format(obtener_sueldo_neto(sueldo), obtener_descuento(sueldo)))


if __name__ == '__main__':
        main()
