#Datos de Entrada
antiguedad = int (input ("Ingresa el valor de antiguedad: "))
#Proceso
if antiguedad<=5:
    bono=antiguedad*100
else:
    bono=1000
#Datos de Salida
print ("Valor de bono: " + repr (bono))