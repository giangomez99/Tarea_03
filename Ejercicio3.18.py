#Datos de Entrada
antiguedad = float (input ("Ingresa el valor de antiguedad: "))
sueldo = float (input ("Ingresa el valor de sueldo: "))
#Proceso
if antiguedad>4 or sueldo<2000:
    bono_navideno=sueldo*0.25
else:
    bono_navideno=sueldo*0.2
#Datos de Salida
print ("Valor de bono navideno: " + repr (bono_navideno))