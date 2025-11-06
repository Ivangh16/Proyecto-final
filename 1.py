n1=(input("El kilo de manzana esta en 50")) 
n2=(input("El kilo de pera esta en 30")) 
n3=(input("El kilo de de platano esta en 25")) 
print=(n1, n2,n3) 
manzana=float (input("¿Cuanto quieres de manzana? ")) 
Pera=float (input("¿Cuanto quieres de pera? ")) 
Platano=float (input ("¿Cuanto quieres de platano? ")) 
if manzana >= 50: 
 print("Compraste mas de un kilo de manzana") 
elif manzana <= 50: 
 print ("Compraste menos de un kilo de manzana") 
if Pera >=30: 
 print("Compraste mas de un kilo de pera") 
elif Pera <=30: 
 print("Compraste menos de un kilo de pera") 
if Platano >= 25: 
 print ("Compraste mas de un kilo de platano") 
elif Platano <=25: 
 print("Compraste menos de un kilo de platano") 
print("Tu total es de", manzana, Pera, Platano)