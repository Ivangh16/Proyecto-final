nombre = input("¿Cuál es tu nombre? ")
print(nombre + ", ¿qué operación deseas hacer?")

ejecutar = True
while ejecutar:
    print("Las opciones son las siguientes:")
    print("Presiona 1 para depositar dinero a tu cuenta")
    print("Presiona 2 para hacer un depósito a otra cuenta")
    print("Presiona 3 para hacer un retiro")
    print("Presiona 4 para consultar tu saldo")
    print("Presiona 5 para pagar algún servicio")
    print("Presiona 6 para terminar la sesión")
    print("*****************************")

    opcion = int(input("Escribe qué opción deseas usar: "))

    if opcion == 1:
        dinero_depositado = float(input("¿Cuanro dinero deseas depositar a tu cuenta? "))
        if dinero_depositado > 10000:
            print("El dinero excede la cantidad permitida")
        else:
            print("Has depositado $" + str(dinero_depositado))
        print("Serás regresado al menú principal")

    elif opcion == 2:
        dinero_otra_cuenta = float(input("¿Cuánto dinero deseas depositar a otra cuenta? Indica e introduzca el dinero por favor "))
        otra_cuenta = int(input("Introduce el número a la cuenta que depositarás "))
        if dinero_otra_cuenta > 10000:
            print("El dinero excede la cantidad permitida")
        else:
            print("Has depositado $" + str(dinero_otra_cuenta) + " a la cuenta", otra_cuenta)
        print("Serás regresado al menú principal")
    
    elif opcion == 3:
        dinero_retirado = float(input("Cuánto dinero deseas retirar? "))
        if dinero_retirado > 1000:
            print("Excediste el limite permitido")
        else:
            print("Has retirado", dinero_retirado, "tu dinero será procesado")
        print("Seras regresado al menú principal")

    elif opcion == 4:
        print("Tu saldo inicial es de 0.0, por favor realiza una transacción o un depósito ")
        print("Serás regresado al menú principal")

    elif opcion == 5:
        print("Servicios disponibles para pagar:")
        print("1. Luz")
        print("2. Agua")
        print("3. Teléfono")
        print("4. Internet")
        servicio = int(input("Selecciona el número del servicio que deseas pagar: "))
        servicio_pago = float(input("¿Cuánto dinero deseas pagar por este servicio? "))
        if servicio_pago > 5000:
            print("El monto excede el límite permitido para pago de servicios")
        else:
            print("Has pagado $" + str(servicio_pago) + " por el servicio seleccionado")
        print("Serás regresado al menú principal")

    elif opcion == 6:
        print("Gracias por usar el sistema, hasta luego", nombre + "!")
        ejecutar = False

    else:
        print("Opción inválida, por favor elige una opción del 1 al 6")
