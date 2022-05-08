#Datos de Entrada
horas_trabajadas = float(input("Ingresa el valor de horas trabajadas: "))
pago_por_hora=float(input("Ingresa el valor de pago por hora: "))
#Proceso
sueldo_semanal=horas_trabajadas*pago_por_hora
if horas_trabajadas>40:
    sueldo_semanal=sueldo_semanal+(horas_trabajadas-40)*pago_por_hora
  #Datos de Salida
print ('Valor de sueldo semanal: ' + repr (sueldo_semanal))