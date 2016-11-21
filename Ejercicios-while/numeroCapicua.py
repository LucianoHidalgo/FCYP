'''
 EJERCICIO : Obtenga por teclado un n�mero entero y determine si el 
 n�mero es capic�a o no.
 
 Un n�mero es capic�a, si puede leerse de derecha a izquierda y de izquieda a derecha del
 mismo modo.
 
 Por ejemplo: 12321 es capic�a y 12000 no lo es.
'''
# BLOQUE PRINCIPAL

# ENTRADA
# Se solicita el ingreso del n�mero 
numero = input("Ingrese el n�mero: ")

# PROCESAMIENTO
# Se determina una variable para ir reduciendo el n�mero 
nuevoNumero = numero
# Se determina una variable, para almacenar el n�mero invertido 
invertido = 0
# Mientras la variable nuevoNumero no sea reducida a cero 
while nuevoNumero > 0 :
	# Para obtener el n�mero invertido, se tendr� el n�mero invertido almacenado
	# anteriormente multiplicado por 10 y el resto de nuevoNumero dividido por 10
	# El objeto de multiplicar por 10 es para dar espacio a la nueva cifra
	# y con el resto de la divisi�n por 10 obtengo la �ltima cifra del n�mero 
    invertido = invertido * 10 + nuevoNumero % 10
	# Divido el nuevoNumero por 10 y lo reasigno a nuevoNumero para 
	# poder obtener la siguiente cifra en la pr�xima iteraci�n
    nuevoNumero = nuevoNumero/10
# Una vez terminado el while

# SALIDA
# reviso si el n�mero original es igual al invertido
if numero == invertido :
	# En caso de serlo, informo que es capicua 
    print "El numero", numero,"es capicua"
# De lo contrario
else:
	# Informo que el n�mero no es capicua
    print "El n�mero",numero,"no es capicua"

	
