# -*- coding: cp1252 -*- 

# ENTRADA
# Solicito el valor del n�mero de punto flotante para trabajar como string
numeroDecimal = raw_input("Ingrese el n�mero deseado: ")
# Solicito la cantidad de decimales que deseo en el texto
decimales = input("Ingrese n�mero de cifras decimales deseadas: ")

# PROCESAMIENTO
redondeado = ""
# Se divide el string por el punto decimal
listaNumeroDecimal = numeroDecimal.split(".")
parteEntera = listaNumeroDecimal[0]
parteDecimal = listaNumeroDecimal[1]

# Busco la cifra decimal siguiente a la cantidad de cifras 
# que deseo y la convierto a entero para 
# su revisi�n de acuerdo a las reglas de redondeo	
numeroARevisar = int(parteDecimal[decimales])


# Si se desea el n�mero sin decimales
if decimales == 0 :
	# Reviso si su primera cifra decimal es igual o superior a 5
	if 	numeroARevisar >= 5 :
		# entrego s�lo su parte entera aumentada en uno
		redondeado = parteEntera + 1
	# De lo contrario
	else :
		# entrego s�lo su parte entera 
		redondeado = parteEntera + 1

# Si se desea un n�mero distinto de cifras
else :

	# Si la cifra siguiente tiene un valor igual o superior a 5
	if  numeroARevisar >= 5:
		# La �ltima cifra del redondeo se aumenta en 1 en su valor
		cifraRedondeada = int(parteDecimal[decimales - 1]) + 1
		# Se construye la parte decimal a partir de los d�gitos 
		# que deseo de la parte decimal actual
		# y de la cifra redondeada
		parteDecimal = parteDecimal[0:decimales - 1] + str(cifraRedondeada)
		# Se construye el n�mero redondeado combinando 
		# la parte entera, la parte decimal y el punto
		redondeado = parteEntera + "." + parteDecimal
	# En caso de que la cifra siguiente no sea igual o superior a 5
	else :
		# Se construye el n�mero redondeado a partir 
		# de la parte entera y los caracteres 
		# deseados de la parte decimal
		redondeado = parteEntera + "." + parteDecimal[0:decimales]

# SALIDA

# Se entrega por pantalla la salida al usuario
print "El valor de", numeroDecimal, "redondeado con ", 
print decimales, "cifras decimales es: "
print "\t", redondeado