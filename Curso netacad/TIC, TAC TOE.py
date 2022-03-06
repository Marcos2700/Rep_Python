from random import randrange
def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
    for fila in board:
        print("+--------" * 3, end="+\n")
        print("|        " * 3, end="|\n")
        cont = 0
        for elem in fila:
            print("|  ", elem, " ", sep="  ", end="")
            cont += 1
        print("|", "\n", end="")
        print("|        " * 3, end="|\n")
    print("+--------" * 3, end="+\n")

def EnterMove(board):
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#
    move = input("Indique su proximo movimiento: ")
    for fila in range(3):
        for elem in range(3):
            if board[fila][elem] == move:
                board[fila][elem] = "O"
                return board
    print("El valor ingresado ya fue escogido, vuelva a intentarlo.")
    EnterMove(board)

def MakeListOfFreeFields(board):
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#
    freeFields = []
    numFila = 1
    for fila in board:
        for elem in fila:
            if elem == "X" or elem == "O":
                continue
            else:
                tup = numFila, elem
                freeFields.append(tup)
        numFila += 1
    return freeFields

def VictoryFor(board, sign):
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#
    cantVert = [0, 0, 0]
    cantHor = [0, 0, 0]
    contHor = 0
    for fila in board:
        contVert = 0
        for elem in fila:
            if elem == sign:
                cantHor[contHor] += 1
                cantVert[contVert] += 1
                contVert += 1
        contHor += 1
    print(cantHor, cantVert)
    for i in cantHor, cantVert:
        freeFields = MakeListOfFreeFields(board)
        print(len(MakeListOfFreeFields(board)))
        if 3 in i:
            if sign == "X":
                print("Ha ganado la maquina")
                return True
            else:
                print("Has ganado")
                return True
        elif len(freeFields) == 2:
            print("Ha terminado en empate")
            return True
        else:
            return False


def DrawMove(board):
#
# la función dibuja el movimient3o de la maquina y actualiza el tablero
#
    move = str(randrange(1, 9))
    for fila in range(3):
        for elem in range(3):
            if board[fila][elem] == move:
                board[fila][elem] = "X"
                return board
    DrawMove(board)

board = [
        ["1", "2", "3"],
        ["4", "X", "6"],
        ["7", "8", "9"]
        ]

while True:
    DisplayBoard(board)
    EnterMove(board)
    DrawMove(board)
    if VictoryFor(board, "O") or VictoryFor(board, "X"):
        DisplayBoard(board)
        break