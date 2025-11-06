#Proyecto Final

#Datos generales
nombre = input("Bienvenido, cuál es tu nombre? ")
print("Perfecto " + nombre + " Vamos a empezar bro")

edad = str(input("Ingresa tu Edad: "))
peso = float(input("Ingresa tu Peso : "))
altura = float(input("Ingresa tu Altura : "))
posicion = input("Ingresa tu Posición (acomodo, libero, banda, central): ").lower()

if posicion == "acomodo":
    print("El acomodo es el cerebro del equipo, arma las jugadas. Necesitas agilidad y precisión")
    print("La Altura recomendada es: 1.70 m - 1.85 m y el IMC ideal: 20 - 23")

elif posicion == "libero":
    print("El libero es el especialista en defensa y recepción. No puede atacar. Necesitas reflejos rápidos")
    print("La Altura recomendada: 1.65 m - 1.80 m y el IMC ideal: 19 - 22")

elif posicion == "banda":
    print("La banda es el Encargado de rematar y bloquear. Requiere fuerza, salto y potencia")
    print("La Altura recomendada: 1.80 m - 1.95 m y el IMC ideal: 21 - 24")

elif posicion == "central":
    print("El central es el jugador más alto. Bloquea y ataca .Necesita fuerza y buen salto")
    print("La Altura recomendada: 1.90 m - 2.10 m y el IMC ideal: 23 - 26")


#Calcular IMC

print("Bien " + nombre + " Ahora calcularemos tu IMC")
print("Esto se calcula dividiendo tu peso entre tu altura al cuadrado ")

IMC = peso/(altura**2)
print("Tu índice de masa corporal es de ", IMC)
if IMC < 18.5:
    estado = "bajo peso"
elif 18.5 <= IMC <= 24.9:
    estado = "peso saludable"
elif 25 <= IMC <= 29.9:
    estado = "sobrepeso"
else:
    estado = "obesidad"

print("Tu estado físico según tu IMC es:", estado)

#Cuidado

comida = int(input("Cuántas veces comes al día? "))
if comida < 3:
    print("Tienes que comer más")
elif comida > 3:
    print("Lo ideal es de 4 a 6 veces, dependiendo de tu entrenamiento")

entrenamiento = int(input("Cuántos días a la semana entrenas?"))
if entrenamiento < 3:
    print("Si eres principiante, lo recomendable es entrenar 4 días")
elif entrenamiento > 3:
    print("Dependiendo de tu objetivo, lo recomendable es entrenar de 4 a 6 días")

salto = float(input("Cuántos centímetros saltas en tu salto vertical? "))
if salto < 40:
    print("Necesitas mejorar tu salto")
elif salto < 55:
    print("Tienes un buen salto, pero puedes mejorarlo.")
else:
    print("Excelente salto, tienes una gran ventaja")

gusto = input("Cuál de estas es tu mayor fortaleza al jugar? (salto, fuerza, velocidad, resistencia): ").lower()
if gusto == salto:
    print("Si eres bueno saltando, te recomiendo jugar de central")
elif gusto == fuerza:
    print("Te recomiendo intentar jugar de banda ")
elif velocidad == velocidad:
    print("Serías bueno jugando como líbero ")
else:
    print("Como acomodador jugarías muy bien, intentalo")









