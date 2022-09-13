# -*- coding: utf-8 -*-
# Reto #3 “Mensaje multilínea”
#Instrucciones: seguro has visto que en Platzi hay más de 600 cursos
# ¿puedes mostrar a que categorías corresponden en una sola línea de código?
#Debe mostrarse así:
#Platzi cuenta con cursos de:
#[categoría1]
#[categoría2]
#[categoría3]
#[categoría4]
#[categoría5]
#[categoría6]

if __name__ == '__main__':
    categorias = ['DESARROLLO E INGENIERIA', 'DISEÑO Y UX', 'MARKETING',
    'NEGOCIOS Y EMPRENDIMIENTO', 'PRODUCCION AUDIVISUAL', 'CRECIMIENTO PROFESIONAL']
    print('Platzi cuenta con cursos de:')
    for categoria in categorias:
        print('{}'.format(categoria))
