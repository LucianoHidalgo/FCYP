# -*- coding: cp1252 -*- 

# ENTRADA

# Solicito la cantidad de n�meros primos
numero = input("Ingrese el valor: ")

# Declaro una lista vac�a para almacenar n�meros primos
listaPrimos = []

# Inicializo el contador en 2 (El primer n�mero primo)
# La idea es usar j para determinar qu� n�meros son primos y cu�les no
j = 2

# Mientras la lista de n�meros primos no tenga la cantidad de n�meros deseada
# EL WHILE EXTERNO BUSCA ALCANZAR UNA LISTA CON LA CANTIDAD DE N�MEROS PRIMOS DESEADA
while len(listaPrimos) < numero :
	# Inicializo el contador i en 2
	# para revisar si un n�mero (j) es primo
    i = 2
    # Declaro una bandera para revisar si el n�mero es primo
    esPrimo = True

    # EL WHILE INTERIOR REVISA SI J ES UN N�MERO PRIMO
    # Mientras no haya revisado todos los n�meros entre 2 y j
    while i < j :
    	# Si el resto de j divido en i es 0
        if j % i == 0 :
        	# Entonces el n�mero no es primo
            esPrimo = False
        # Incremento el valor de i para seguir revisando si j 
        # cumple las condiciones para ser un n�mero primo
        i = i + 1
    
    # Si j es primo (Es decir no se encontraron divisores exactos entre i = 2 e i = j - 1)
    if esPrimo :
    	# Agrego j a listaPrimos
        listaPrimos.append(j)
    # Incremento el valor de j para seguir buscando n�meros primos
    j = j + 1

# SALIDA
# Imprimo la cantidad de n�meros primos solicitada
print listaPrimos
