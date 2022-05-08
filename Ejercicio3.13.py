#Datos de Entrada
numero_de_alumnos = int (input ("Ingresa el valor de numero de alumnos: "))
costo_del_pasaje=70
#Proceso
if numero_de_alumnos>=20:
    costo_del_pasaje=40
if numero_de_alumnos>=40:
    costo_del_pasaje=35
if numero_de_alumnos>100:
    costo_del_pasaje=20
#Datos de Salida
print ("Valor de costo del pasaje: " + repr (costo_del_pasaje))