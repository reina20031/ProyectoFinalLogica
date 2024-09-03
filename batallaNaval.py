import random 

def crearTablero(dimension):
    return [["~" for _ in range(dimension)] for _ in range(dimension)]

def mostrarTableros(tableroDisparosjugador, tableroDisparosOponente):
    print("\n tablero de disparos:")
    for fila in tableroDisparosjugador:
        print(" ".join(fila))
    print("\n Tablero de disparos del Oponente: ")
    for fila in tableroDisparosOponente:
        print(" ".join(fila))

def colocarbarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado = False
        while not colocado:
            if jugador == "jugador":
                print(f"colocado {barco['nombre']} de tamaño {barco['dimension']}")
                fila= int(input("ingrese la fila: "))
                columna = int(input("ingrese la columna: "))
                orientacion = input("ingrese la orientacion (h para horizontal, v para vertical): ").lower()
            else:
                fila = random.randint(0, len(tablero)-1)
                columna = random.randint(0, len(tablero)-1)
                orientacion = random.choice(['h', 'v'])


            if validarColocacion(tablero, fila, columna, barco['dimension'], orientacion):
                colocarbarco(tablero, fila, columna, barco['dimension'], orientacion)
                colocado = True 
            elif jugador == "jugador":
                print("colocacion es invalida. intenta de nuevo")

def validarColocacion(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        if columna + dimension > len(tablero):
            return False 
        for i in range(dimension):
            if tablero[fila][columna+i] != "~":
                 return False
    else:
        if fila + dimension>len(tablero):
            return False
        for i in range (dimension):
            if tablero[fila+i][columna] != "~":
                return False
    return True

def colocarbarco(tablero, fila, columna, dimension, orientacion):
    if orientacion == 'h':
        for i in range(dimension):
            tablero[fila][columna+i]="B"
    else:
        for i in range(dimension):
            tablero[fila+i][columna]="B"

def realizarDisparo(tableroOculto, tableroDisparos, fila, columna):
    if tableroOculto[fila][columna] == "B":
        tableroDisparos[fila][columna] = "X"
        tableroOculto[fila][columna] = "H"
        return "impacto"
    elif tableroDisparos[fila][columna] == "~":
        tableroDisparos[fila][columna] = "O"
        return "Agua"
    return "Ya disparaste aqui"

def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:
            return False
    return True 

def jugarContraComputadora():
    dimension = 5 
    tableroJugador = crearTablero(dimension)
    tableroComputadora = crearTablero(dimension)
    tableroDisparosJugador = crearTablero(dimension)
    tableroDisparosComputadora = crearTablero(dimension)
    barcos = [
        {"nombre":"PortaAviones", "dimension":3},
        {"nombre":"Submarino", "dimension":2}
    ]
    print("coloca tus barcos")
    colocarbarcos(tableroJugador, barcos, "jugador")
    colocarbarcos(tableroComputadora, barcos,"computadora")
    turnoJugador=True
    while True:
        if turnoJugador:
            print("\n Tu turno")
            mostrarTableros(tableroDisparosJugador, tableroDisparosComputadora)
            fila = int(input("Ingresa la fila del disparo: "))
            columna = int(input("Ingresa la columna del disparo: "))
            resultado = realizarDisparo(tableroComputadora, tableroDisparosJugador, fila, columna)
            print(resultado)
            if verificarVictoria(tableroComputadora):
                print("Ganaste")
                return "Jugador"
        else:
            print("\n Turno de la computadora")
            fila = random.randint(0, dimension-1)
            columna = random.randint(0, dimension-1)
            resultado = realizarDisparo(tableroJugador, tableroDisparosComputadora, fila, columna)
            print(f"La computadora disparo en ({fila}, {columna}): {resultado} ")
            if verificarVictoria(tableroJugador):
                print("La computadora gano ")
                return "Computadora"
        turnojugar = not turnoJugador
            
            
def jugarDosJugadores():
    dimension = 5 
    tableroJugador1 = crearTablero(dimension)
    tableroJugador2 = crearTablero(dimension)
    tableroComputadora2 = crearTablero(dimension)
    tableroDisparosJugador1 = crearTablero(dimension)
    tableroDisparosJugador2 = crearTablero(dimension)
    barcos = [
        {"nombre":"PortaAviones", "dimension":3},
        {"nombre":"Submarino", "dimension":2}
    ]
    print("Jugador 1 coloca tus barcos")
    colocarbarcos(tableroJugador1, barcos, "jugador")
    print("Jugador 2 coloca tus barcos")
    colocarbarcos(tableroJugador2, barcos,"computadora")
    turnoJugador=True
    while True:
        if turnoJugador:
            print("\nTu turno")
            mostrarTableros(tableroDisparosJugador1, tableroDisparosJugador2)
            fila = int(input("Ingresa la fila del disparo: "))
            columna = int(input("Ingresa la columna del disparo: "))
            resultado = realizarDisparo(tableroJugador2, tableroJugador1, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador2):
                print("Ganaste")
                return "Jugador"
        else:
            print("\n Turno de la computadora")
            fila = random.randint(0, dimension-1)
            columna = random.randint(0, dimension-1)
            resultado = realizarDisparo(tableroJugador1, tableroDisparosJugador2, fila, columna)
            print(resultado)
            if verificarVictoria(tableroJugador2):
                print("La computadora gano ")
                return "Computadora"
        turnojugar1 = not turnojugar1 

def mostrarMenu():
    print("Bienvenido a Batalla Naval!!! ")
    print("Selecciona contra quien Jugaras ")
    print("1. Contra computadora")
    print("2. Contra otro Jugador")
    print("3. Salir")

def IniciarJuego():
    while True:
        mostrarMenu()
        modo = input("Elige una opcion: ")
        if modo == "1":
            ganador = jugarContraComputadora()
        elif modo == "2":
            ganador = jugarDosJugadores()
        elif modo == "3":
            print("Gracias por jugar con Pio Pio")
            break
        else:
            print("Opcion no valida, por favor eliga una opcion correcta")
            continue
        print(f"El ganador es {ganador}")
        JugarDeNuevo = input("Quieres jugar de nuevo? (s/n): ").lower()
        if JugarDeNuevo !="s":
            print("Gracias por jugar, hasta la vista baby")
            break

IniciarJuego()
1
            