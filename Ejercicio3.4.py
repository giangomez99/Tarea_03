#Datos de Entrada
horas = int (input ('Ingresa el valor de horas: '))
cobro=0
#Proceso
if horas<=2:
    cobro=horas*5
if horas>2 and horas<=5:
    cobro=2*5+(horas-2)*4
if horas>5 and horas<=10:
    cobro=2*5+3*4+(horas-5)*3
if horas>10:
    cobro=2*5+3*4+3*5+(horas-10)*2
#Datos de salida
print ('Valor de cobro: ' + repr (cobro))