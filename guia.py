ejercicio = int(input("Ingrese el ejercicio a revisar (opciones del 1 al 9) : "))
if ejercicio == 1:
	#Ejercicio 1
	#!/usr/bin/env python
	# -*- coding: utf-8 -*-
	nombre = raw_input("Ingresa tu nombre : ")
	edad = int(input("Ingresa tu edad :"))
	print "Bienvenido ",nombre, " tienes una edad de ", edad, " anhos lo sufiente para que puedas entender python!" 
elif ejercicio == 2:
	# Ejercicio 2
	c = float(input("Ingrese un la temperatura a convertir: "))
	print "La temperatura ", c," grados celcius en grados Kelvin es :" , 273+c, "grados"
	print "La temperatura ", c," grados celcius en grados Fahrenheit es : " ,((9*c)/5)+32, "grados"
elif ejercicio == 3:
	# Ejercicio 3
	n1 = float(input("Ingrese el primer numero : "))
	n2 = float(input("Ingrese el segundo numero : "))
	n3 = float(input("Ingrese el tercer numero : "))

	if ((n1 > n2) and (n1 > n3)):
		print "El mayor numero es : ", n1
	if ((n2 > n1) and (n2 > n3)):
		print "El mayor numero es : ",n2
	if ((n3 > n2) and (n3 > n1)):
		print "El mayor numero es : ",n3
	else:
		print "los numeros son iguales : ", n1
elif ejercicio == 4:
#Ejercicio 4
	f = int(input("Ingrese el numero a calcular su factorial: "))
	if f > 1:
		f*=f-1
	print "El factorial del numero es : ",f
elif ejercicio == 5:
#Ejercicio 5
	n1 = int(input("Ingrese el primer numero : "))
	n2 = int(input("Ingrese el segundo numero : "))
	n3 = int(input("Ingrese el tercer numero : "))
	print "El minimo comun multiplo entre : ", n1, "," , n2, ",", n3, " es ", n1*n2*n3
elif ejercicio == 6:
#Ejercicio 6
	s = int(input("Ingrese un numero para calcular la serie :"))
	se = 0
	while (s > 1):
		n = float(s-1)
		d = float (s)
		se = se+float(n/d)
		s -= 1
	print "La serie es : ",se+1

#Ejercicio 8
elif ejercicio == 8:
	cc = int(input("Ingrese la cantida de casas que se censaran : "))
	cmee = 0
	cmae = 0
	while cc > 0:
		cp = int(input("Ingrese la cantidad de personas que viven en la casa: "))
		while cp > 0:
			ep = int(input("Ingrese la edad de la persona: "))
			if ep < 18:
				cmee +=1
			else:
				cmae +=1
			cp -=1
		cc-=1
	print "La cantidad de personas mayores de edad censadas es ",cmae
	print "La cantidad de personas menores de edad censadas es ",cmee

#elif ejercicio == 9:
	#Ejercicio 9

	#cp = int(input("Ingrese la cantidad de personas a participar en el terreo : "))
	#cht = int(input("Ingrese la cantidad de horas que durara el terreo : "))
	#vsp = 0.0
	#vnb = 0.0
	# se sabe que por cada hora de tarreo se consumen en total 5 articulos independiente de la
	# cantidad de participantes del tarreo.
	#if (cht >= 3):
		#Se aplica factor de descuento en supermercado
		#vsp = (1490*cht+1350*cht*2+990*cht+560*cht)*0.88
		#vnb = (1390*cht+1150*2*cht+950*cht+500*cht)
		#if (vsp > vnb):
		#	print "Es mas conveniente comprar en el negocio del barrio, se gastara un total de :",vnb," el ahorro total es de :",vnb-vsp," cada uno debe aportar: ", (float(vnb)/float(cp)
		#else (vsp < vnb):
		#	print "Es mas conveniente comprar en el supermercado, se gastara un total de :",vsp, "el ahorro total es de :",vsp-vnb," cada uno debe aportar: " (float(vsp)/float(cp)
	#else:
		#print"Da igual donde commprar ya que el valor es mismo, cada uno debe aportar : " (float(vnb)/float(cp)) 

else:
	print "Ingreso una opcion no valida, adios..."
