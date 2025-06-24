"""Esse metodo é o matemático"""
"""co = float(input('Digite o comprimento do cateto Oposto: '))
ca = float(input('Digite o comprimenjto do Cateto Adjacente: '))
hi = (co ** 2 + ca **2) ** (1/2)
print('A hipotenusa vai medir  {:.2f}'.format(hi))"""

""" import math
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o compriemnto do Cateto Adajacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f} '.format(hi))"""


from math import hypot
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o compriemnto do Cateto Adajacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f} '.format(hi))
