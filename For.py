nombres = ["Luisa", "Daniela", "Iván", "Jacobo", "Sam"]
for nombre in nombres:
    print("Hola " + nombre + " Fabuloso día ")

print("Luisa tiene 15 años")
print("Daniela tiene 16 años")
print("Iván tiene 17 años")
print("Jacobo tiene 18 años")
print("Sam tiene 19 años")

numeros = [15, 16, 17, 18, 19]
referencia = 17
for numero in numeros:
    if numero > referencia:
        print( numero, "es mayor que Jacobo", referencia)
    elif numero == referencia:
        print(numero, "Jacobo tiene la edad de Jacobo JAJAJA", referencia)
    else:
        print(numero, "es menor que Jacobo", referencia)