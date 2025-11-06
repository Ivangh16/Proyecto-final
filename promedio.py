#Calcular el promedio
Quimica = float(input("Escribe tu última calificación de quimica "))
Ingles = float(input("Dime como te fue en tu ultimo examen de ingles "))
Historia = float(input("Cuanto sacaste en tu examen de medio termino en historia? "))
Mate = float(input("Como te fue en el mid-term exam de mate? "))
Español = float(input("Escribe tu promedio de español "))
PLC = float(input("Cuanto sacaste en tu ultima actividad de plc? "))
promedio = float(int(Quimica + Ingles + Historia + Mate + Español + PLC)/6)
print("tu promedio es de ", promedio)
if promedio > 70:
    print("Tu promedio actual es aprobatorio")
if promedio <70:
    print("Tu promedio actual es reprobatorio")