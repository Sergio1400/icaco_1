#Horas y tarifa
Horas = 8
Tarifa = 200
#Ejercicios
#Sueldo bruto
Bruto = Tarifa * Horas
#Descuento 1
ESSALUD = Bruto * 0.09
#Descuento 2
AFP = Bruto * 0.10
#Descuento total
Descuento_total = ESSALUD + AFP
#Sueldo neto
Neto = Bruto - Descuento_total

print("Horas: ",Horas)
print("Tarifa: ",Tarifa)
print("Sueldo bruto: ",Bruto)
print("Descuento de ESSALUD: ",ESSALUD)
print("Descuento de AFP: ",AFP)
print("Descuento total: ",Descuento_total)
print("Sueldo neto: ",Neto)