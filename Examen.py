
print("Hola! Bienvenido a la tiendaATM contamos con un buen catalgo")
nombre = str(input("¿Cuál es tu nombre bro? "))
print("Perfecto " + nombre + " Vamos a comprar!")

total = 0  
descuento = 0
mensualidad = 0
total_final = 0

ejecutar = True
while ejecutar:

    print("***********")
    print("Nuestros productos son:")
    print("Playeras")
    print("Jeans")
    print("Tenis")
    print("Sudaderas")
    print("Cinturones")
    print("****************")

    ropa_comprar = str(input("¿Qué tipo de ropa deseas comprar? "))

    if ropa_comprar == "Playeras":
        print("Las playeras tienen un costo de $149, tenemos tallas chicas, medianas y grandes ")
        total += 149

    elif ropa_comprar == "Jeans":
        print("Nuestros Jeans cuestan $849, manejamos las tallas XS/34, S/36, M/40, L/44, XL/46 ")
        total += 849

    elif ropa_comprar == "Tenis":
        print("Tenemos tenis desde 23cm hasta 29 cm, los modelos cuestan $2500 ")
        total += 2500

    elif ropa_comprar == "Sudaderas":
        print("Todas las sudaderas, independientemente del tamaño (Ch, M, G) cuestan $1000 ")
        total += 1000

    elif ropa_comprar == "Cinturones":
        print("Estos accesorios cuestan $300")
        total += 300

    else:
        print("Producto no disponible, por favor elige uno de la lista.")

    continuar = input("¿Deseas seguir comprando? ")
    if continuar == "no":
        ejecutar = False


print("Ahora procederemos con el pago, manejamos efectivo, tarjeta o transferencia ")
print("Si el pago lo realiza con tarjeta, sea débito o crédito, puede pagar a 12 meses sin Intereses ")
print("Si realiza el pago de contado, cuenta con el 10% de descuento ")

print("Tu total actual es de: $", total)

pago = str(input("Cómo deseas pagar? Con efectivo, tarjeta o transferencia? "))

if pago == "efectivo":
    descuento = total * 0.10
    total_final = total - descuento
    print("Tienes un 10% de descuento. Total a pagar: $", total_final)

elif pago == "tarjeta":
    mensualidad = total / 12
    total_final = total
    print("Pagando con tarjeta puedes hacerlo a 12 meses sin intereses.")
    print("Son 12 pagos de $", mensualidad)

elif pago == "transferencia":
    total_final = total
    print("Perfecto, el total a transferir es de: $", total)
    print("La cuenta disponible para la transferencia es 123456789")

else:
    print("Método de pago no válido, intenta de nuevo.")


print("Tu ticket es el siguiente:")
print("**********************")
print("Tiendas ATM S.A de C.V")
print("Tienda Av. Lago de Guadalupe K.M. 3.5")
print("General de ley de personas morales")
print("¡Gracias por tu compra " + nombre + "!")
print("Tu método de pago es: " + pago)
print("Tu descuento es de: $" + str(descuento))
print("Tu total a pagar con MSI son: $" + str(mensualidad))
print("************************")
print("Tu total es de: $" + str(total_final))
