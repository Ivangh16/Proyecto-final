
print("Bienvenidos a un cuento de terror")
nombre = input("Escribe tu nombre para saber quien es el protagonista: ")
print(nombre + ", vamos a empezar")
print("Presiona 1 si quieres la experiencia completa")
print("Presiona 2 si te da un poco de miedo y lo quieres moderado")
print("Presiona 3 si te da aún más miedo y lo quieres menos fuerte")
print("Presiona 4 si de verdad quieres un cuento super leve")
print("Presiona 5 si no quieres nada")

ejecutar = True
while ejecutar:
    opcion = int(input("Selecciona una opción: "))

    if opcion == 1:
        print("¡Vaya... qué valiente!")
        cuento_uno = input("¿Qué personaje quieres que salga en tu historia: Annabelle, Slenderman o la Monja? ")

        if cuento_uno == "Annabelle":
            print("Tu historia tratará de Annabelle")
        elif cuento_uno == "Slenderman":
            print("Tu historia tratará de Slenderman")
        elif cuento_uno == "la Monja":
            print("Tu historia tratará de la Monja")

        lugar = input("¿Te gustaría que tu historia se desenvolviera en: una casa, un parque o una escuela abandonada? ")

        if lugar == "una casa":
            print("Escogiste una casa")
        elif lugar == "un parque":
            print("Escogiste un parque")
        elif lugar == "una escuela abandonada":
            print("Escogiste una escuela abandonada")

        print("Esta historia se desarrolla en " + lugar + " donde " + cuento_uno + " ataca durante la noche...")
        print("Has muerto, regresarás al inicio")

    elif opcion == 2:
        print("Ok, moderado será")
        cuento_dos = input("¿Qué personaje quieres que salga en tu historia: Chucky, la Llorona o el Jinete sin cabeza? ")

        if cuento_dos == "Chucky":
            print("Tu historia tratará de Chucky")
        elif cuento_dos == "la Llorona":
            print("Tu historia tratará de la Llorona")
        elif cuento_dos == "el Jinete sin cabeza":
            print("Tu historia tratará del Jinete sin cabeza")

        lugar_dos = input("¿Te gustaría que tu historia se desenvolviera en: Hospital, un cementerio o un parque acuático? ")

        if lugar_dos == "Hospital":
            print("Escogiste un Hospital")
        elif lugar_dos == "un cementerio":
            print("Escogiste un cementerio")
        elif lugar_dos == "un parque acuático":
            print("Escogiste un parque acuático")

        print("Esta historia se desarrolla en " + lugar_dos + ", cuando " + cuento_dos + " ataca durante la noche...")

    elif opcion == 3:
        print("Ok, no pasa nada. Menos fuerte será")
        cuento_tres = input("¿Qué personaje quieres que salga en tu historia: Pennywise, Ghostface o Hannibal Lecter? ")

        if cuento_tres == "Pennywise":
            print("Escogiste a Pennywise")
        elif cuento_tres == "Ghostface":
            print("Escogiste a Ghostface")
        elif cuento_tres == "Hannibal Lecter":
            print("Escogiste a Hannibal Lecter")

        lugar_tres = input("¿Te gustaría que tu historia se desenvolviera en: un Restaurante, un orfanato o una cárcel? ")

        if lugar_tres == "un Restaurante":
            print("Escogiste un Restaurante")
        elif lugar_tres == "un orfanato":
            print("Escogiste un orfanato")
        elif lugar_tres == "una cárcel":
            print("Escogiste una cárcel")

        print("Esta historia se desarrolla en " + lugar_tres + ", cuando " + cuento_tres + " ataca durante la noche...")

    elif opcion == 4:
        print("Será súper leve ")
        cuento_cuatro = input("¿Qué personaje quieres que aparezca: Drácula, Nemesis o Momias? ")

        if cuento_cuatro == "Drácula":
            print("Escogiste a Drácula")
        elif cuento_cuatro == "Nemesis":
            print("Escogiste a Nemesis")
        elif cuento_cuatro == "Momias":
            print("Escogiste a Momias")

        lugar_cuatro = input("¿Dónde quieres que se desarrolle tu historia: un salón de clases, una cafetería o un supermercado? ")

        if lugar_cuatro == "un salón de clases":
            print("Escogiste un salón de clases")
        elif lugar_cuatro == "una cafetería":
            print("Escogiste una cafetería")
        elif lugar_cuatro == "un supermercado":
            print("Escogiste un supermercado")

        print("Esta historia habla de " + cuento_cuatro + " en " + lugar_cuatro + " donde ataca de noche...")

    elif opcion == 5:
        print("Perfecto, deseaste ser feliz!")
        ejecutar = False























                   
        