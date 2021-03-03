# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:39:39 2021

@author: William Medina

"""

# 1. Hacer un algoritmo que calcule el total a pagar por la compra de
# camisas. Si se compran tres camisas o mas se aplica un descuento
# del 30% sobre el total de la compra y si son menos de tres camisas
# un descuento del 10%.


camisa = int(input('Ingrese el numero de camisas a comprar: '))
valor_camisa = float(input('Ingrese el valor de cada camisa: '))


if(camisa > 0 and camisa < 3):
    descuento = (valor_camisa * camisa) * 0.10
    valor_pagar = (valor_camisa * camisa) - descuento
elif (camisa >= 3):
    descuento = (valor_camisa * camisa) * 0.30
    valor_pagar = (valor_camisa * camisa) - descuento

print(f'El valor a pagar por la(s) {camisa} camisa(s) es ${valor_pagar} ')

# 2. En un supermercado se hace una promoción, mediante la cual el
# cliente obtiene un descuento dependiendo de un número que se
# escoge al azar. Si el número escogido es menor que 74 el descuento
# es del 15% sobre el total de la compra, si es mayor o igual a 74 el
# descuento es del 20%. Obtener cuanto dinero se le descuenta.

numero = int(input('Ingrese el número escogido por el cliente '))
valor_compra = float(input('Ingrese el valor de la compra '))

if(numero < 74):
    descuento = valor_compra * 0.15
elif (numero >= 74):
    descuento = valor_compra * 0.20

print(f'El valor descontado de ${valor_compra} es ${descuento}')

# 3. Una compañía de seguros está abriendo un departamento de
# finanzas y estableció un programa para captar clientes, que conssite
# en lo siguiente: Si el monto por el que se efectúa la fianza es menor
# que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
# es mayor que $50.000 la cuota a pagar será el 2% del monto. La
# afianzadora desea determinar cual será la cuota que debe pagar al
# cliente.


monto = float(input('Ingrese el monto de la fianza: '))
if(monto < 50000):
    cuota = monto * 0.03
elif(monto > 50000):
    cuota = monto * 0.02

print(f'La cuota que el cliente debe pagar es ${cuota}')


# 4. Una fábrica ha sido sometida a un programa de control de
# contaminación para lo cual se efectúa una revisión de los puntos de
# contaminación generados por la fábrica. El programa de control de
# contaminación consiste en medir los puntos que emite la fábrica en
# cinco días de una semana y si el promedio es superior a los 170
# puntos entonces tendrá la sanción de parar su producción por una
# semana y una multa del 50% de las ganancias diarias cuando no se
# detiene la producción. Si el promedio obtenido de puntos es de 170 o
# menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
# desea saber cuanto dinero perderá después de ser sometido a la
# revisión.

# Puntos por dia
dia_1 = int(input('Ingrese la cantidad de puntos registrados en el dia 1 '))
dia_2 = int(input('Ingrese la cantidad de puntos registrados en el dia 2 '))
dia_3 = int(input('Ingrese la cantidad de puntos registrados en el dia 3 '))
dia_4 = int(input('Ingrese la cantidad de puntos registrados en el dia 4 '))
dia_5 = int(input('Ingrese la cantidad de puntos registrados en el dia 5 '))

suma_puntos = dia_1 + dia_2 + dia_3 + dia_4 + dia_5
promedio = suma_puntos / 5
valor_multa = 0
dinero_perdido = 0

if(promedio > 170):
    dias_produccion = int(input('Ingrese dias de producción '))
    ganancias = float(input(f'Ingrese valor de ganancias por {dias_produccion} dias '))
    valor_multa = (ganancias / dias_produccion) * 0.5
    dinero_perdido = valor_multa * dias_produccion
    print(f' Usted tiene una sanción de parar su producción por una semana')
    print(f' El valor de la multa diaria es ${valor_multa}')
    print(f' El dinero perdido despues de la revisión es ${dinero_perdido}')
    
elif(promedio <= 170):
     print(f' El valor de la multa diaria es ${valor_multa}')
     print(f' El dinero perdido despues de la revisión es ${valor_multa}')
    
# 5. Una persona se encuentra con un problema de comprar un automóvil
# o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
# mientras el automóvil se devalúa, con el terreno sucede lo contrario.
# Esta persona comprará el automóvil si al cabo de tres años la
# devaluación de este no es mayor que la mitad del incremento del
# valor del terreno. Ayúdale a esta persona a determinar si debe o no
# comprar el automóvil.

valor_activo = float(input('Ingrese el valor del activo '))
porc_auto = float(input('Ingrese el porcentaje anual de depreciación del automovil '))
porc_terr = float(input('Ingrese el porcentaje anual de valorización del terreno '))

total_dev_auto = valor_activo * ((porc_auto * 3) / 100)
total_val_terr = valor_activo * ((porc_terr * 3) / 100)

if(total_dev_auto < (total_val_terr / 2)):
    print(f' La persona debe comprar el automovil porque el valor de \n'
          f'${total_dev_auto} devaluado es menor que la mitad del valor \n'
          f'que es ${total_val_terr / 2} valorizado del terreno')
else:
    print(f' La persona no debe comprar el automovil porque el valor de \n'
          f'${total_dev_auto} devaluado es mayor que la mitad del valor \n'
          f' que es${total_val_terr / 2} valorizado del terreno')


# 6. En una fábrica de computadoras se planea ofrecer a los clientes un
# descuento que dependerá del número de computadoreas que
# compre. Si las computadoras son menos de cinco se les dará un 10%
# de descuento sobre el total de la compra; si el número de
# computadoras es mayor o igual a cinco pero menos de diez se le
# otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
# precio de cada computadora es de $11.000.

numero_pc = int(input('Ingrese el número de computadoras a comprar '))

if(numero_pc < 5):
    descuento = (numero_pc * 11000) * 0.1
elif(numero_pc >= 5 and numero_pc < 10):
    descuento = (numero_pc * 11000) * 0.2
elif(numero_pc >= 10):
    descuento = (numero_pc * 11000) * 0.4
    
print(f'El descuento aplicado por {numero_pc} computadores es ${descuento} \n'
      f'y el valor a pagar es {(numero_pc * 11000) - descuento} ')
        
        
    
# 7. Un proveedor de estéreos ofrece un descuento del 10% sobre el
# precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
# independientemente de esto, ofrece un 5% de descuento si la marca
# es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
# cualquiera por la compra de su aparato. IVA es del 16%.

val_aparato = float(input('Ingrese valor del aparato '))
nosy = input('Ingrese "si" si es marca Nosy o "no" si no lo es: ')
descuento = 0

if(val_aparato >= 2000):
    descuento = val_aparato * 0.1
    if(nosy == 'si'):
        total_pagar = ((val_aparato - descuento) * 0.95) + (val_aparato * 0.16)
        print(f'El valor total a pagar es ${total_pagar}')
    else:
        total_pagar = (val_aparato - descuento) + (val_aparato * 0.16)
        print(f'El valor total a pagar es ${total_pagar}')
else:
    if(nosy == 'si'):
        total_pagar = val_aparato - (val_aparato * 0.05) + (val_aparato * 0.16)
        print(f'El valor total a pagar es ${total_pagar}')
    else:
        print(f'El valor total a pagar es ${val_aparato + (val_aparato * 0.16)}')
        
# 8. Una empresa quiere hacer una compra de varias piezas de la misma
# clase a una fábrica de refacciones. La empresa, dependiendo del
# monto total de la compra, decidirá que hacer para pagar al fabricante.
# Si el monto total de la compra excede de $500.000 la empresa tendrá
# la capacidad de invertir de su propio dinero un 55% del monto de la
# compra, pedir prestado al banco un 30% y el resto lo pagará
# solicitando un crédito al fabricante. Si el monto total de la compra no
# excede de $500.00 la empresa tendrá capacidad de invertir de su
# propio dinero un 70% y el restante 30% lo pagará solicitando crédito
# al fabricante. El fabricante cobra por concepto de interes un 20%
# sobre la cantidad que se le pague a crédito. Obtener la cantidad a
# inverir, valor del préstamo, valor del crédito y los intereses.

monto_compra = float(input('Ingrese el monto de la compra '))


if (monto_compra > 500000):
    inversion = (monto_compra * 0.55)
    prestamo = (monto_compra * 0.3)
    credito = (monto_compra * 0.15)
    intereses = (credito * 0.2) + credito
else:
    inversion = (monto_compra * 0.7)
    credito = (monto_compra * 0.3)
    intereses = (credito * 0.2) + credito
    
print(f'La cantidad a invertir es ${inversion}')
print(f'El valor del prestamo es ${prestamo}')
print(f'El valor del credito es ${credito}')
print(f'El valor de los intereses son ${intereses}')

    
# 9. Leer 2 números; si son iguales que lo multiplique, si el primero es
# mayor que el segundo que los reste y sino que los sume.

num_1 = int(input('Ingrese el primer número '))
num_2 = int(input('Ingrese el segundo número '))

if(num_1 == num_2):
    operacion = num_1 * num_2
elif(num_1 > num_2):
    operacion = num_1 - num_2
else: 
    operacion = num_1 + num_2
    
print(f'El resultado de la operacion es {operacion}')

# 10. Leer tres números diferentes e imprimir el número mayor de los
# tres.
        
numero_1 = float(input("Ingrese el primer numero "))
numero_2 = float(input("Digite el segundo numero "))
numero_3 = float(input("Digite el tercer numero "))

if ((numero_1 == numero_2 or numero_1 == numero_3) or (numero_2 == numero_3 or numero_2 == numero_1)):
    print("Los numeros deben ser diferentes")
elif (numero_1 > numero_2 and numero_1 > numero_3):    
     print(f"El numero {numero_1} es el mayor")
elif (numero_2 > numero_1 and numero_2 > numero_3):    
     print(f"El numero {numero_2} es el mayor")
elif (numero_3 > numero_2 and numero_3 > numero_1):    
     print(f"El numero {numero_3} es el mayor")


    



    
    
