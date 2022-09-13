# -*- coding: utf-8 -*-

#Reto #7 - Mensajes opcionales
#Crearás un un script para el que el usuario indicará un número entre 1 y 6.
#Como respuesta se le brindará un mensaje según el número leido:
#1 - “Hoy aprenderemos sobre prorgamación”
#2 - “¿Qué tal tomar un curso de marketing digital?
#3 - “Hoy es un gran día para comenzar a aprender de diseño”
#4 - ¿Y si aprendemos algo de negocios online?
#5 - “Veamos un par de clases sobre producción audiovisual”
#6 - “Tal vez sea bueno desarrollar una habilidad blanda en Platzi”
#En caso indicar un número distinto, pedir al usuario que ingrese uno en el rango válido.

def switch(case):
   sw = {
      1: "Hoy aprenderemos sobre prorgamación",
      2: "¿Qué tal tomar un curso de marketing digital?",
      3: "Hoy es un gran día para comenzar a aprender de diseño",
      4: '¿Y si aprendemos algo de negocios online?',
      5: 'Veamos un par de clases sobre producción audiovisual',
      6: 'Tal vez sea bueno desarrollar una habilidad blanda en Platzi'
   }
   return sw.get(case, default())

def default():
   return "rango invalido ingrese otro numero"


if __name__ == '__main__':

    while True:
        numero = int(raw_input('Indique un numero: '))
        print(switch(numero))
