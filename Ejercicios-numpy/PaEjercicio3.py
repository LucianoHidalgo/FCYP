# IMPORTACI�N DE MODULOS

# Se importa el m�dulo numpy
import numpy
# Se importa el m�dulo matplotlib.pyplot
import matplotlib.pyplot as plotter

# CONSTANTES
# Se declaran los tres casos a graficar
VALOR_R0_CASO_1 = 0.5
VALOR_R0_CASO_2 = 1.0
VALOR_R0_CASO_3 = 1.5

# Se importa desde numpy el valor de PI 
PI = numpy.pi 
# Se declara el salto que tendr� el vector de �ngulos
SALTO = 0.0001

# ENTRADAS
# No existen entradas, pues todos los valores entregados
# son constantes


# PROCESO

# Se genera el vector para el �ngulo en el intervalo
# de -PI a PI
angulo = numpy.arange(-PI, PI + SALTO, SALTO)

# Para el caso 1
# Se determina el valor de r para r0 = 0.5
vectorR0Caso1 = VALOR_R0_CASO_1 + numpy.cos(angulo)
# Se genera el vector para el eje X
vectorXCaso1 = vectorR0Caso1 * numpy.cos(angulo)
# Se genera el vector para el eje y
vectorYCaso1 = vectorR0Caso1 * numpy.sin(angulo)

# Para el caso 2
# Se determina el valor de r para r0 = 1.0
vectorR0Caso2 = VALOR_R0_CASO_2 + numpy.cos(angulo)
# Se genera el vector para el eje X
vectorXCaso2 = vectorR0Caso2 * numpy.cos(angulo)
# Se genera el vector para el eje y
vectorYCaso2 = vectorR0Caso2 * numpy.sin(angulo)

# Para el caso 3
# Se determina el valor de r para r0 = 1.5
vectorR0Caso3 = VALOR_R0_CASO_3 + numpy.cos(angulo)
# Se genera el vector para el eje X
vectorXCaso3 = vectorR0Caso3 * numpy.cos(angulo)
# Se genera el vector para el eje y
vectorYCaso3 = vectorR0Caso3 * numpy.sin(angulo)

#SALIDAS

# Se grafica la primera curva con r0 = 0.5
curva1 = plotter.plot(vectorXCaso1, vectorYCaso1)
# Se setea el color de la l�nea en rojo
plotter.setp(curva1, 'color', 'r')

# Se grafica la segunda curva con r0 = 1.0
curva2 = plotter.plot(vectorXCaso2, vectorYCaso2)
# Se setea el color de la l�nea en verde
plotter.setp(curva1, 'color', 'g')

# Se grafica la tercera curva con r0 = 1.5
curva3 = plotter.plot(vectorXCaso3, vectorYCaso3)
# Se setea el color de la l�nea en azul
plotter.setp(curva1, 'color', 'b')

# Se le agrega un t�tulo al gr�fico
plotter.title("Grafico de caracoles de pascal")

# Se le agrega un r�tulo al eje X
plotter.xlabel("r cos(angulo)")
# Se le agrega un r�tulo al eje Y
plotter.ylabel("r sin(angulo)")
# Se muestra el gr�fico
plotter.show()