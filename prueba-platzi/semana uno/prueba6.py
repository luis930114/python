# -*- coding: utf-8 -*-
#Reto #6 “Resta de pizzas”
#Instrucciones: llegaste a una fiesta con X cantidad de rebanadas de pizza (indicadas por el usuario),
#después de un rato se consumió Y cantidad de rebanadas y quedan Z. Fácil ¿cierto?
#El reto está en que expreses lo que sucede es una forma comprensible para cualquier persona,
#imprescindible pensar en tus usuarios 😉

if __name__ == '__main__' :
      rebanadas = int(raw_input("escriba el numero de rebanadas de pizza: "))
      print('traje {} rebanadas de pizza'.format(rebanadas))

      cant_rebanadas_comidas = int(raw_input("escriba el numero de rebanadas de pizza: "))
      cantidad_rebanadas_faltantes = rebanadas - cant_rebanadas_comidas
      print('se han comido {} y faltan por comer {}'.
      format(cant_rebanadas_comidas, cantidad_rebanadas_faltantes))
