#!/usr/bin/env python
# -*- coding: utf-8 -*-
while True:
	ne1=0
	ne2=0
	ne3=0
	ne4=0
	ne5=0
	ne6=0
	ne8=0
	ne9=0
	nf=0
	ejercicio = int(input("Ingrese el ejercicio a revisar (opciones del 1 al 9, 0 para salir) : "))
	if ejercicio == 1:
		#Ejercicio 1
		#!/usr/bin/env python
		# -*- coding: utf-8 -*-
		nombre = input("Ingresa tu nombre : ")
		edad = int(input("Ingresa tu edad : "))
		print ("Bienvenido ",nombre, " tienes una edad de ", edad, " anhos, lo sufiente para que puedas revisar esta tarea hecha en python" )
		ne1 = float(input("Ingresa la nota del ejercicio 1 :"))
	elif ejercicio == 2:
		# Ejercicio 2
		c = float(input("Ingrese un la temperatura en grados Celcius a convertir: "))
		print ("La temperatura ", c," grados celcius en grados Kelvin es :" , 273+c, "grados")
		print ("La temperatura ", c," grados celcius en grados Fahrenheit es : " ,((9*c)/5)+32, "grados")
		ne2 = float(input("Ingresa la nota del ejercicio 2 :"))
	elif ejercicio == 3:
		# Ejercicio 3
		n1 = float(input("Ingresa el primer numero : "))
		n2 = float(input("Ingresa el segundo numero : "))
		n3 = float(input("Ingresa el tercer numero : "))

		if ((n1 > n2) and (n1 > n3)):
			print ("El mayor numero es : ", n1)
		if ((n2 > n1) and (n2 > n3)):
			print ("El mayor numero es : ",n2)
		if ((n3 > n2) and (n3 > n1)):
			print ("El mayor numero es : ",n3)
		else:
			print ("Los numeros son iguales : ", n1)
		ne3 = float(input("Ingresa la nota del ejercicio 3 :"))
	elif ejercicio == 4:
	#Ejercicio 4
		f = int(input("Ingresa el numero a calcular su factorial: "))
		if f > 1:
			f*=f*f-1
		print ("El factorial del numero es : ",f)
		ne4 = float(input("Ingresa la nota del ejercicio 4 :"))
	elif ejercicio == 5:
	#Ejercicio 5
		n1 = int(input("Ingresa el primer numero : "))
		n2 = int(input("Ingresa el segundo numero : "))
		n3 = int(input("Ingresa el tercer numero : "))
		print ("El minimo comun multiplo entre : ", n1, "," , n2, ",", n3, " es ", n1*n2*n3)
		ne5 = float(input("Ingresa la nota del ejercicio 5 :"))
	elif ejercicio == 6:
	#Ejercicio 6
		s = int(input("Ingresa un numero para calcular la serie :"))
		se = 0
		while (s > 1):
			n = float(s-1)
			d = float (s)
			se = se+float(n/d)
			s -= 1
		print ("La serie es : ",se+1)
		ne6 = float(input("Ingresa la nota del ejercicio 6 :"))

	#Ejercicio 8
	elif ejercicio == 8:
		cc = int(input("Ingresa la cantida de casas que se censaran : "))
		cmee = 0
		cmae = 0
		while cc > 0:
			cp = int(input("Ingresa la cantidad de personas que viven en la casa: "))
			while cp > 0:
				ep = int(input("Ingresa la edad de la persona: "))
				if ep < 18:
					cmee +=1
				else:
					cmae +=1
				cp -=1
			cc-=1
		print ("La cantidad de personas mayores de edad censadas es ",cmae)
		print ("La cantidad de personas menores de edad censadas es ",cmee)
		ne8 = float(input("Ingresa la nota del ejercicio 8 :"))
	elif ejercicio == 9:
		#Ejercicio 9
		cp = int(input("Ingrese la cantidad de personas a participar en el terreo : "))
		cht = int(input("Ingrese la cantidad de horas que durara el terreo : "))
		vsp = 0.0
		vnb = 0.0
		# se sabe que por cada hora de tarreo se consumen en total 5 articulos independiente de la
		# cantidad de participantes del tarreo.
		if (cht >= 3):
			#Se aplica factor de descuento en supermercado
			vsp = (1490*cht+1350*cht*2+990*cht+560*cht)*0.88
			vnb = (1390*cht+1150*2*cht+950*cht+500*cht)
			if (vsp > vnb):
				convertir = (float(vnb)/float(cp))
				print ("Es mas conveniente comprar en el negocio del barrio, se gastara un total de :",vnb, " el ahorro total es de : ",vsp-vnb," cada uno debe aportar: "+str(convertir))
			elif (vsp < vnb):
				convertir = (float(vsp)/float(cp))
				print ("Es mas conveniente comprar en el supermercado, se gastara un total de :",vsp, "el ahorro total es de :", vnb-vsp," cada uno debe aportar: " +str(convertir))
			else:
				print ("Da igual donde commprar ya que el valor es mismo, cada uno debe aportar : " (float(vnb)/float(cp)))	
		else:
			vnb = (1390*cht+1150*2*cht+950*cht+500*cht)
			print("Es mas barato comprar en el negocio de barrio, sale un total de : ",vnb," y cada uno debe aportar con : ",(float(vnb)/float(cp))," pesos")
		ne9 = float(input("Ingrese la nota del ejercicio 9: "))

	elif ejercicio == 0:
		nf=float((ne1+ne2+ne3+ne4+ne5+ne6+ne8+ne9)/8)
		if (nf<4):
			print("Creo que existe un error favor volver a compilar y revisar nuevamente")
			break
		else:
			print ("La nota obtenida es :", nf, "Gracias por revisar")
			break
