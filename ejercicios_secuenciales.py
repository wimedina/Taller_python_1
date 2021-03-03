# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:46:44 2021

@author: Wiliam Medina
"""

# 1.Tres personas deciden invertir su dinero para fundar una empresa.
# Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje
# que cada quien invierte con respecto a la cantidad total invertida.

total_invertido = float(input('Ingrese el valor de la inversion total: '))

porcentaje_1 = ((total_invertido*0.25)*100) / total_invertido
porcentaje_2 = ((total_invertido*0.45)*100) / total_invertido
porcentaje_3 = ((total_invertido*0.30)*100) / total_invertido

print(f' La persona 1 invierte {porcentaje_1} % del total')
print(f' La persona 2 invierte {porcentaje_2} % del total')
print(f' La persona 3 invierte {porcentaje_3} % del total')


# 2. Una empresa paga a sus empleados además del sueldo base una
# bonificación especial de $80.000 por cada hijo. Realice un programa
# en Java que determine el monto de la bonificación y el monto total a
# pagar al trabajador.

sueldo = float(input('Ingrese el sueldo del empleado: '))
num_hijos = int(input('Ingrese el número de hijos del empleado: '))
bonificacion = num_hijos * 80000
print(f'la bonificación total del empleado es {bonificacion}')
print(f' El monto total a pagar es ${sueldo + bonificacion} ')

# 3. Un banco da a sus ahorradores un interes de 1.5% sobre el monto
# ahorrado. Teniendo como dato de entrada el saldo inicial del
# ahorrador determine el saldo final.

saldo_inicial = float(input('Ingrese el saldo inicial a ahorrar: '))
saldo_final = saldo_inicial + (saldo_inicial * 0.015)
print(f' El saldo final con el interés es ${saldo_final}')

# 4. Una inmobiliria vende terrenos a $80.000 el metro cuadrado. El
# cliente debe dar una cuota inicial del 35%y el resto lo paga en 12
# cuotas. Determine el valor a pagar por cuota inicial y el monto de
# cada cuota.

metros_cuadrados = int(input('Ingrese el número de metros cuadrados: '))
valor_total = metros_cuadrados * 80000
cuota_inicial = valor_total * 0.35
monto_cuota = (valor_total * 0.65) / 12
print(f' El valor de la cuota inicial es ${cuota_inicial}')
print(f' El valor de las cuotas restantes es ${monto_cuota}')

# 5.Una empresa le hace los siguientes descuentos sobre el sueldo base
# a sus trabajadores: 1% por ley de politica pública, 4% por seguro
# social, 0.5% por seguro forzoso y 5% por caja de ahorro. Realice un
# programa en Java que determine el monto de cada descuento y el
# monto total a pagar al trabajador.

sueldo = float(input('Ingrese el sueldo del empleado '))
desc_politica = sueldo * 0.01
desc_seg_social = sueldo * 0.04
desc_seg_forzoso = sueldo * 0.005
desc_caja_ahorro = sueldo * 0.05
total_pagar = sueldo - (desc_politica + desc_seg_social + desc_seg_forzoso + desc_caja_ahorro)
print(f' El descuento por política pública es ${desc_politica}')
print(f' El descuento por seguro social es ${desc_seg_social} ')
print(f' El descuento por seguro forsozo es ${desc_seg_forzoso}')
print(f' El descuento por caja de ahorro es ${desc_caja_ahorro}')
print(f' El total a pagar es ${total_pagar}')

# 6. El periódico el Informador cobra por un aviso clasificado un monto
# que depende del número de palabras, tamaño en cetímetros y
# número de colores. Cada palabra tiene un costo de $20.000, cada
# centímetro tiene un costo de $15.000 y cada color tiene un costo de
# $25.000. Realice un algoritmo que determine el monto a pagar por un
# aviso clasificado.

palabras = int(input('Ingrese el número de palabras del aviso: '))
centimetros = int(input('Ingrese el número de centímetros del aviso: '))
color = int(input('Ingrese el número de colores que desea para el aviso: '))
total_palabras = palabras * 20000
total_centimetros = centimetros * 15000
total_color = color * 25000
total_pagar = total_palabras + total_centimetros + total_color
print(f'El monto a pagar por el aviso es ${total_pagar}')


# 7. Una empresa paga a sus empleados un bono por antigüedad que
# consiste en $100.000 por el primer año laboral y $120.000 por cada
# año siguiente. Realice un programa en Java que determine el monto
# del bono a pagar a un trabajador que tiene varios años en la empresa.

antiguedad = int(input('Ingrese la antiguedad del empleado en años '))
monto_bono = antiguedad * 120000
print(f'El monto total a pagar del bono es ${monto_bono}')

# 8. Una Universidad le paga a sus profesores $20.000 la hora y le hace
# un descuento del 5% por concepto de caja de ahorro. Determine el
# monto del descuento y el monto total a pagar al profesor.

horas_laboradas = int(input('Ingrese el número de horas laboradas '))
subtotal = horas_laboradas * 20000
descuento = subtotal * 0.05
total = subtotal - descuento
print(f'El descuento por caja de ahorro es ${descuento}')
print(f'El monto total a pagar al profesor es ${total}')

# 9. Un centro de comunicaciones alquilan tarjetas para realizar llamadas
# y cobran el monto consumido de la tarjeta mas un recargo del 20%.
# Teniendo como dato de entrada el monto inicial y el monto final de la
# tarjeta, determine el costo de la llamada.

monto_inicial = float(input('Ingrese el monto inicial de la tarjeta '))
monto_final = float(input('Ingrese el monto final de la tarjeta '))

subtotal_monto = monto_inicial - monto_final
total = subtotal_monto + (subtotal_monto * 0.2)
print(f'El costo final de la llamada es ${total}')

# 10. En una fototienda cobran por el revelado de un rollo $1.500 por cada
# foto. Realice un programa en Python que determine el monto a pagar
# por un revelado completo sabiendo que adiconalmente le cobran el
# IVA (16%).

foto = int(input('Ingrese el número de fotos a revelar: '))
subtotal = foto * 1500
total = subtotal + (subtotal * 0.16)
print(f'El monto a pagar es ${total}')

# 11. En un hospital existen tres áreas: Ginecología, Pediatría y
# Traumatología. El presupuesto anual del hospital se reparte
# conforme a la siguiente tabla:
# Area Porcentaje Presupuestal
# Ginecología 40%
# Traumatología 30%
# Pediatría 30%
# Obtener la cantidad de dinero que recibirá cada área, para cualquier
# monto presupuestal.

presupuesto = float(input('Ingrese el presupuesto anual: '))
print(f'El area de ginecología recibira ${presupuesto * 0.40}')
print(f'El area de traumatología recibira ${presupuesto * 0.30}')
print(f'El area de pediatría recibira ${presupuesto * 0.30}')

# 12. Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
# que consiste en dejar gratis el alquiler de una película. Realice un
# programa en Python que teniendo como dato de entrada el total de
# películas alquiladas, y el número de días de alquiler, determine el
# monto a pagar.

peliculas = int(input('Ingrese el número de peliculas alquiladas: '))
dias_alquiler = int(input('Ingrese el número de dias de alquiler: '))
subtotal = peliculas * 1500
total = subtotal * dias
print(f'El monto a pagar es ${total}')

#13. Una Agencia de viajes cobra por un Tour a Cartagena $25.000
# diarios por persona. Realice un programa en Java que determine el
# monto a pagar por una familia que desee realizar dicho Tour
# sabiendo que también cobran el 12% de IVA.

personas = int(input('Ingrese el número de personas: '))
dias = int(input('Ingrese el número de dias del tour: '))
total_x_dia = personas * 25000
subtotal = total_x_dia * dias
total = subtotal + (subtotal * 0.12)
print(f' Total a pagar por el tour: ${total}')


#14. Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
# clientes. Cobra por una habitación $100.000 el primer día y por el
# resto $200.000 por día. Realice un programa en Java que determine
# el valor total a pagar por la habitación si la estadía fue de varios
# días.

dias_estadia = int(input('Ingrese el número de dias de estancia: '))
dia_1 = dias_estadia - (dias_estadia - 1)
resto_dias = dias_estadia - dia_1
total_resto_dias = resto_dias * 200000
print(f'El valor a pagar por los {dias_estadia} dias es de ${total_resto_dias + 100000} ')

# 15. El banco del Pueblo da microcréditos a empresarios para ser
# cancelados en un lapso de 2 años (24 meses). Al monto del
# préstamo se le cobra un interés del 24%. El empresario debe pagar
# la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20
# cuotas ordinarias. Realice un algoritmo que teniendo como dato de
# entrada el monto del préstamo, determine el monto total a pagar por
# el préstamo, el monto de las cuotas especiales y el monto de las
# cuotas ordinarias.


monto_prestamo = float(input('Ingrese el monto total del prestamo '))
total_pagar = monto_prestamo + (monto_prestamo * 0.24)
cuota_especial = (total_pagar / 2 ) / 4
cuota_ordinaria = (total_pagar / 2) / 20
print(f'El monto total a pagar es ${total_pagar}')
print(f'El monto de las cuotas especiales es ${cuota_especial}')
print(f'El monto de las cuotas ordinarias es ${cuota_ordinaria}')






