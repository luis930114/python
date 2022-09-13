# -*- coding: utf-8 -*-
# Reto #8 “Divide la cuenta”
#Instrucciones: vas con tus amigos a tu restaurante favorito y acuerdan dividir la cuenta.
#Para facilitar las cosa pedirás al usuario que indique el total a pagar,
#entre cuantas personas se dvidirá la cuenta, porcentaje de propina a incluir,
#un porcentaje de impuestos,
#total a pagar incluyendo propina más impuestos y el total a pagar por cada persona.

def divide_pago(pago, num_personas, impuestos_propina, impuestos):
    #pago de impuestos_propina
    propina = pago * impuestos_propina
    #pago de impuestos
    pago_impuesto = pago * impuestos
    total = pago + propina + pago_impuesto
    print('el total a pagar es de {}'.format(total))
    total_persona = total / num_personas
    print('el total a pagar de cada persona es de {}'.format(total_persona))


if __name__ == '__main__':
    total = float(raw_input("total a pagar de la  cuenta: "))
    num_personas = int(raw_input("numero de personas a pagar la cuenta: "))
    porcentaje_propina = float(raw_input("digite el porcentaje de la propina de la  cuenta: "))
    impuestos = float(raw_input("digite el porcentaje de impuestos de la  cuenta: "))

    divide_pago(total, num_personas, porcentaje_propina, impuestos)
