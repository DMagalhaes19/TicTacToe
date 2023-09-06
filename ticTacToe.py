import random

#global variables
board = []
player = ""
computer = ""
turn = ""
gameOver = False
gameMode = 0
boardSize = 0
score = [0,0,0] #player wins, computer wins, ties

#function to create the board
def createBoard():
    global boardSize
    for i in range(boardSize):
        board.append([])
        for j in range(boardSize):
            board[i].append(" ")
    return board

#function to print the board
def printBoard():
    global boardSize
    for i in range(boardSize):
        print(" ---" * boardSize)
        print("|", end="")
        for j in range(boardSize):
            print(" " + board[i][j] + " |", end="")
        print()
    print(" ---" * boardSize)

#function to check if the board is full
def isBoardFull():
    global boardSize
    for i in range(boardSize):
        for j in range(boardSize):
            if board[i][j] == " ":
                return False
    return True

#function to check if the player has won
def checkPlayerWin():
    global boardSize
    #check rows
    for i in range(boardSize):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    #check columns
    for i in range(boardSize):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

#function to check if the computer has won
def checkComputerWin():
    global boardSize
    #check rows
    for i in range(boardSize):
        if board[i][0] == board[i][1] == board[i][2] == computer:
            return True
    #check columns
    for i in range(boardSize):
        if board[0][i] == board[1][i] == board[2][i] == computer:
            return True
    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] == computer:
        return True
    if board[0][2] == board[1][1] == board[2][0] == computer:
        return True
    return False

#function to check if the game is over
def checkGameOver():
    global gameOver
    if checkPlayerWin() or checkComputerWin() or isBoardFull():
        gameOver = True
        return True
    return False

#function to check if the player is trying to make an illegal move
def checkIllegalMove(row, col):
    global boardSize
    if row < 0 or row >= boardSize or col < 0 or col >= boardSize:
        return True
    if board[row][col] != " ":
        return True
    return False

#function to get the player's move
def getPlayerMove():
    global boardSize
    while True:
        try:
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
            if checkIllegalMove(row, col):
                print("Illegal move. Try again.")
                continue
            board[row][col] = player
            break
        except:
            print("Invalid input. Try again.")

#function to get the computer's move
def getComputerMove():
    global boardSize
    while True:
        row = random.randint(0, boardSize - 1)
        col = random.randint(0, boardSize - 1)
        if checkIllegalMove(row, col):
            continue
        board[row][col] = computer
        break

#function to get the computer's move using the minimax algorithm
def getComputerMoveMinimax():
    global boardSize
    bestScore = -1000
    bestMove = [-1, -1]
    for i in range(boardSize):
        for j in range(boardSize):
            if board[i][j] == " ":
                board[i][j] = computer
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > bestScore:
                    bestScore = score
                    bestMove = [i, j]
    board[bestMove[0]][bestMove[1]] = computer

#function to get the score of the board
def getScore():
    global boardSize
    if checkPlayerWin():
        return -10
    elif checkComputerWin():
        return 10
    elif isBoardFull():
        return 0
    
#function to get the best score of the board
def minimax(board, depth, isMaximizing):
    global boardSize
    score = getScore()
    if score != None:
        return score
    if isMaximizing:
        bestScore = -1000
        for i in range(boardSize):
            for j in range(boardSize):
                if board[i][j] == " ":
                    board[i][j] = computer
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    if score > bestScore:
                        bestScore = score
        return bestScore
    else:
        bestScore = 1000
        for i in range(boardSize):
            for j in range(boardSize):
                if board[i][j] == " ":
                    board[i][j] = player
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    if score < bestScore:
                        bestScore = score
        return bestScore
    
#function to reset the board
def resetBoard():
    global board
    board = []
    createBoard()

#function to reset the game
def resetGame():
    global gameOver
    global score
    gameOver = False
    score = [0,0,0]
    resetBoard()

#function to change the game mode
def changeGameMode():
    global gameMode
    while True:
        try:
            gameMode = int(input("Enter the game mode (1 player or 2 player): "))
            if gameMode < 1 or gameMode > 2:
                print("Invalid input. Try again.")
                continue
            break
        except:
            print("Invalid input. Try again.")

#function to change the board size
def changeBoardSize():
    global boardSize
    while True:
        try:
            boardSize = int(input("Enter the board size: "))
            if boardSize < 3:
                print("Invalid input. Try again.")
                continue
            break
        except:
            print("Invalid input. Try again.")

#function to change the game piece
def changeGamePiece():
    global player
    global computer
    while True:
        player = input("Enter the player's game piece: ")
        if player == "":
            print("Invalid input. Try again.")
            continue
        break
    while True:
        computer = input("Enter the computer's game piece: ")
        if computer == "":
            print("Invalid input. Try again.")
            continue
        break



#main function
def main():
    while True:
        changeGameMode()
        changeBoardSize()
        changeGamePiece()
        resetGame()
        printBoard()
        while not gameOver:
            if gameMode == 1:
                getPlayerMove()
                printBoard()
                if checkGameOver():
                    break
                getComputerMoveMinimax()
                printBoard()
            elif gameMode == 2:
                getPlayerMove()
                printBoard()
                if checkGameOver():
                    break
                getPlayerMove()
                printBoard()
        if checkPlayerWin():
            print("Player wins!")
            score[0] += 1
        elif checkComputerWin():
            print("Computer wins!")
            score[1] += 1
        elif isBoardFull():
            print("Tie!")
            score[2] += 1
        print("Player wins: " + str(score[0]))
        print("Computer wins: " + str(score[1]))
        print("Ties: " + str(score[2]))
        while True:
            try:
                choice = int(input("Enter 1 to play again or 2 to quit: "))
                if choice < 1 or choice > 2:
                    print("Invalid input. Try again.")
                    continue
                break
            except:
                print("Invalid input. Try again.")
        if choice == 1:
            resetBoard()
            printBoard()
            continue
        elif choice == 2:
            break

main()
