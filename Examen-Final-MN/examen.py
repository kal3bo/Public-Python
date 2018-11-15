from __future__ import division                 #Para versiones anteriores a Python 3.4
import math

#Metodo Random:
numero = 9
k = 13091206342165455000
weyl = 0
cont = 0

def random_number():
    global numero
    global k
    global weyl

    numero = numero * numero
    weyl += k
    numero += weyl
    numero = (numero >> 32) | (numero << 32)
    corteA = int((len(str(numero)) - 16) / 2)
    numero = str(numero)[corteA : corteA + 16]
    numero = int(numero)

    num = str(numero)
    if len(num) == 15:
        num = '.0' + num
    else:
        num = '.' + num
    num = float(num)

    return num
