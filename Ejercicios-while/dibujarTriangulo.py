# -*- coding: cp1252 -*- 

'''
# Entrada
numero = input("Ingrese la cantidad de l�neas: ")

# Proceso y salida

# Se inicia un contador para las filas de la figura
i = 0

# Mientras no se escriba el n�mero de filas de la figura
while i < numero :
	# Se inicia un contador para las columnas de la figura
	j = 0
	# Mientras no se escriba el n�mero adecuado de caracteres
	while j < numero - i :
		# Si el caracter va en una columna par
		if j % 2 == 0 :
			# Se escribe un #
			print "#",
		# Si el caracter se escribe en una columna impar
		else : 
			# Se escribe una O
			print "O",
			# Los print llevan coma para que el siguiente caracter
			# se escriba en la misma l�nea
		# Se incrementa el contador de j, para escribir la l�nea completa
		j = j + 1
	# Se imprime un salto de l�nea, una vez escrita una l�nea
	print "\n",
	# Se incrementa el contador de i, para escribir cada una de las filas
	i = i + 1

'''

####################################################################################
#
# SOLUCI�N USANDO S�LAMENTE UN PRINT
#
####################################################################################

# Entrada
numero = input("Ingrese la cantidad de l�neas: ")

# Proceso 

# Se inicia un contador para las filas de la figura
i = 0

# Se inicializa un string vac�o para almacenar la figura
figura = ""

# Mientras no se escriba el n�mero de filas de la figura
while i < numero :
	# Se inicia un contador para las columnas de la figura
	j = 0
	# Mientras no se escriba el n�mero adecuado de caracteres
	while j < numero - i :
		# Si el caracter va en una columna par
		if j % 2 == 0 :
			# Se a�ade un # al string
			figura = figura + "#"
		# Si el caracter se escribe en una columna impar
		else : 
			# Se a�ade una O al string
			figura = figura + "O"
			# Los print llevan coma para que el siguiente caracter
			# se escriba en la misma l�nea
		# Se incrementa el contador de j, para escribir la l�nea completa
		j = j + 1
	# Se a�ade un salto de l�nea a la figura
	figura = figura + "\n"
	# Se incrementa el contador de i, para escribir cada una de las filas
	i = i + 1

# Salida
print figura