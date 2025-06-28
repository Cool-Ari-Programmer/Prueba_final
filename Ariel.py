# Variables ---------------------

zapatollas_reservadas = 0
zapatollas_restantes = 20
lista_de_reservas = [
    {"nombre": "placeholder", "zapatillas_reservadas": 0}
]
reserva = {
    
}
input_user = 0
busca_reserva = False
nombre = 0
nombre_buscar = 0
frase_usuario = "plaiholdel"
frase_secreta = "EstoyEnListaDeReserva"

# Variables/ ---------------------

while True:
    print("BIENVENIDO A EL TOTEM DE RESERVA DE ZAPATILLAS")
    print("Opcion [1]: Reservar Zapatillas")
    print("Opcion [2]: Buscar reserva de Zapatillas")
    print("Opcion [3]: Ver stock actual")
    print("Opcion [4]: Salir")

    input_user = input()

    try:
        input_user = int(input_user)
    except ValueError:
        print("Por favor, ingresa un número válido.")

        continue

    if input_user == 1:
        if zapatollas_restantes > 0:
            nombre = input("Ingresa tu nombre: ")
            frase_usuario = input("Ingresa la frase secreta: ")
            if frase_usuario == frase_secreta:
                reserva = {
                "nombre": nombre,
                "zapatillas_reservadas": 1
                }
                lista_de_reservas.append(reserva)
                zapatollas_reservadas = zapatollas_reservadas + 1
                zapatollas_restantes = zapatollas_restantes - 1
            else:
                print("La frase secreta esta mala, no se le a cobrado ni hecho la reserva")
        else:
            print("No hay zapatillas disponibles para reservar.")

    elif input_user == 2:
        nombre_buscar = input("Ingresa el nombre de la reserva: ")
        
        busca_reserva = False
        for reserva in lista_de_reservas:
            if reserva["nombre"] == nombre_buscar :
                print(f"Reserva encontrada: {reserva}")
                busca_reserva = True
                
                while True:
                        print("Te gustaria pagar extra para reservar una otro par de zapatillas? ([1] Si ; [2] No)")
                        input_user = input()
                        try:
                            input_user = int(input_user)
                        except ValueError:
                            print("Por favor, ingresa un número válido.")
                            continue
                        if input_user == 1:
                            zapatollas_reservadas = zapatollas_reservadas +1
                            zapatollas_restantes = zapatollas_restantes -1 
                            reserva["zapatillas_reservadas"] += 1
                            print("Un par extra de zapatillas ha sido reservado")
                            break
                        elif input_user == 2:
                            
                            print("Usted a elegido no, no se le a cobrado")
                            break
                        else:
                            print("Porfavor ingresar una opcion valida")
        if not busca_reserva:
            print("No se encontró una reserva con ese nombre y apellido.")
    elif input_user == 3:
        print(f"Zapatillas reservadas: {zapatollas_reservadas}")
        print(f"Zapatillas restantes: {zapatollas_restantes}")
    elif input_user == 4:
        break
    elif input_user == 5:
        print(lista_de_reservas)