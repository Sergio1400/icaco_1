#Donacion
Hospital = 1000
#Descuentos
#1
General = Hospital * 0.45
#2
Gine = General * 0.80
#3
General_Gine = General + Gine
Pedi = General_Gine * 0.20
#4
Trau = Hospital - General - Gine - Pedi

print("Donacion: ",Hospital)
print("Medicina General: ",General)
print("Ginecologia: ",Gine)
print("Pediatria: ",Pedi)
print("Traumatología: ",Trau)