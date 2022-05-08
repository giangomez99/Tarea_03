#Datos de Entrada
precio = float (input ("Ingresa el valor de precio: "))
descuento=0
#Proceso
if precio>=200:
    descuento=precio*0.15
if precio>100 and precio<200:
    descuento=precio*0.12
if precio<100:
    descuento=precio*0.1
costo=precio-descuento
#Datos de Salida
print ("Valor de costo: " + repr (costo))
print ("Valor de descuento: " + repr (descuento))