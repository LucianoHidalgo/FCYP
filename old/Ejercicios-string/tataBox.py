'''
PREGUNTA:

Una caja TATA es una secuencia de ADN encontrada en varios organismos vivos.

Comienza siempre con �TATAAA�. Siempre sigue con tres o m�s A�s en m�ltiplos de tres, es decir, TATAAAAAA es una caja TATA, pues contiene 6 letras A, pero TATAAAAA no lo es, pues s�lo contiene 5.

Construya una funci�n en Python que reciba como entrada una secuencia de ADN como string y entregue la mayor secuencia de la caja TATA. Su soluci�n debe funcionar para cualquier secuencia de ADN. Los datos del ejemplo son solo referenciales

Por ejemplo: 
�	Para el string �ATTTGATGATAATTTATAAAAAAAAAATGATAAATA�
�	La caja TATA est� ubicada en:
 ATTTGATGATAATTTATAAAAAAAAAATGATAAATA 
�	y por lo tanto, la funci�n deber�a entregar: TATAAAAAAAAA

Considere que se debe entregar siempre la secuencia TATA de mayor tama�o en el texto. 

'''
# SOLUCI�N

# Funci�n que entrega la mayor caja TATAAA encontrada en 
# una secuencia de ADN
# ENTRADA: Secuencia de ADN (string)
# SALIDA: Caja TATAAA de mayor tama�o (string)
def encontrarCajaTata(secuencia):
	# Determino el patr�n a buscar
	cajaTata = "TATAAA"
	# Si no encuentro el patr�n en la secuencia
	if not (cajaTata in secuencia):
		# Se entrega un string vac�o
		return ""
	# Mientras la caja TATAAA se encuentre en la secuencia de ADN 
	while cajaTata in secuencia :
		# Se agregan 3 A a la caja a buscar 
		cajaTataNueva = cajaTata + "AAA"
		# Si el patrón con las 3 AAA no se encuentra
		if not (cajaTataNueva in secuencia) :
			# Se retorna el patr�n anterior
			return cajaTata
		# En caso contrario
		else :
			# Se contin�a la b�squeda con el nuevo patr�n
			cajaTata = cajaTataNueva
	
	











from random import random, randint









TEMPERATURAS_MAXIMAS = []

while len(TEMPERATURAS_MAXIMAS) < 365 :
	temp = randint(-3,36) + round(random(),1)
	TEMPERATURAS_MAXIMAS.append(temp)

# Función que ordena una lista
# ENTRADA: Lista de elementos
# SALIDA: Lista de elementos ordenados
def ordenarLista(lista):
	# Se declara una lista vacía para agregar los elementos ordenados 
	listaOrdenada = []
	# Mientras queden elementos en la lista
	while len(lista) > 0 :
		# Se determina un valor mínimo como el elemento inicial de la lista
		minimo = lista[0]
		# Se declara un iterador para encontrar el mínimo 
		i = 0
		# Mientras i no alcance el largo de la lista 
		while i < len(lista) :
			# Si el minimo es mayor que el elemento a revisar
			if minimo > lista[i]:
				# Se cambia el valor del mínimo 
				minimo = lista[i]
			# Se incrementa el valor de i 
			i = i + 1
		# Se agrega el mínimo a la lista ordenada 
		listaOrdenada.append(minimo)
		# Se elimina el elemento de la lista original 
		lista.remove(minimo)
	# Se retorna la lista ordenada 
	return listaOrdenada
	
#
# BLOQUE PRINCIPAL
#

# ENTRADA
# Se solicita la cantidad de elementos a buscar  
entrada = input("Ingrese la cantidad de elementos:")

# PROCESO
# Se declara una lista vacía para las n temperaturas 
temperaturas = []
# Se ordena la lista de temperaturas máximas 
temperaturasOrdenadas = ordenarLista(TEMPERATURAS_MAXIMAS)
# Se declara un iterador para ir agregando los n elementos del final 
i = 1
# Mientras i no alcance el valor de la entrada 
while i <= entrada :
	# Se agrega el valor a la lista de temperaturas 
	temperaturas.append(temperaturasOrdenadas[-i])
	# Se incrementa el valor de i 
	i = i + 1

# Se imprimen las n temperaturas más altas
print "Las", entrada, "temperaturas más altas del año son: ", temperaturas


