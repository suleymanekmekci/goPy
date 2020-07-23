gameSize = int(input("What Size Game GoPy?"))
totalSize = gameSize ** 2
numbers = [num for num in range(totalSize + 1)]
matrix = []
for i in range(0,len(numbers)-1,gameSize):
    matrix.append(numbers[i: i+gameSize])

lastnumber = []
def printMatrix(myList):
    for row in myList:

        print("".join([(' ' if len(str(x))> 1 else '  '  )+str(x) for x in row]))
    
printMatrix(matrix)
    
def gameFinishX():
    rowElements = ["X" * gameSize]
    gameFinish = []
    for a in rowElements[0]:
        gameFinish.append(a)
    
    #row check
    for row in matrix:
        if row == gameFinish:
            return True

    x = 0
    #column check
    while x < gameSize:
        currentColumn = []
        y = 0 #second argument
        while y < gameSize:
            count = 0
            if matrix[y][x] == "X":
                currentColumn.append(matrix[y][x])
                if gameFinish == currentColumn:
                    return True
            y+= 1
        x += 1
    
    #left to the right diagonal
    x = 0
    y = 0
    currentDiagonal = [] 
    while x < gameSize:
        if matrix[y][x] == "X":
            currentDiagonal.append(matrix[y][x])
            if gameFinish == currentDiagonal:
                return True
        x , y = x+1 , y+1

    #right to the left diagonal
    x = 0
    y = gameSize - 1
    currentDiagonal = []
    while x < gameSize:
        if matrix[x][y] == "X":
            currentDiagonal.append(matrix[x][y])
            if gameFinish == currentDiagonal:
                return True
        x, y = x+1 , y-1

def gameFinishO():
    rowElements = ["O" * gameSize]
    gameFinish = []
    for a in rowElements[0]:
        gameFinish.append(a)

    #check the row
    for row in matrix:
        if row == gameFinish:
            return True
    
    #check the column
    x = 0 #first argument
    while x < gameSize:
        currentColumn = []
        y = 0 #second argument
        while y < gameSize:
            count = 0
            if matrix[y][x] == "O":
                currentColumn.append(matrix[y][x])
                if gameFinish == currentColumn:
                    return True
            y+= 1
        x += 1

    #left to the right diagonal
    x = 0
    y = 0
    currentDiagonal = [] 
    while x < gameSize:
        if matrix[y][x] == "O":
            currentDiagonal.append(matrix[y][x])
            if gameFinish == currentDiagonal:
                return True
        x , y = x+1 , y+1
    
    #right to the left diagonal
    x = 0
    y = gameSize - 1
    currentDiagonal = []
    while x < gameSize:
        if matrix[x][y] == "O":
            currentDiagonal.append(matrix[x][y])
            if gameFinish == currentDiagonal:
                return True
        x, y = x+1 , y-1

pickedNumbers = {}    
def playerChoice(playerChoice,playerNumber):
    a = 0

    while a < gameSize:
        b = 0
        while b < gameSize:
            if matrix[a][b] == playerChoice and  playerNumber == 1:
                if matrix[a][b] == playerChoice:
                    
                    pickedNumbers[playerChoice] = 'X'
                    matrix[a][b] = "X"

                    
            elif matrix[a][b] == playerChoice and playerNumber == 2:
                if matrix[a][b] == playerChoice:
                    pickedNumbers[playerChoice] = 'O'
                    matrix[a][b] = "O"
            b += 1
        a += 1
 
def checkMove(playerChoice,playerNumber):
    
    if playerNumber == 1:
        try:
            if pickedNumbers[playerChoice] == 'X':
                print("You have made this choice before")
            elif pickedNumbers[playerChoice] == 'O':
                print("The other player select this cell before")
        except KeyError:
            pass
    elif playerNumber == 2:
        try:
            if pickedNumbers[playerChoice] == 'O':
                print("You have made this choice before")
            elif pickedNumbers[playerChoice] == 'X':
                print("The other player select this cell before")
        except KeyError:
            pass

def checkGameFinish():
    currentMatrix = []
    for row in matrix:
        for number in row:
            currentMatrix.append(number)
    count = 0
    for i in numbers:
        if i in currentMatrix:
            count += 1

    if count == 0:
        print("No winner")
        return True
    else:
        return False 

while True:
    #player1
    player1Input = int(input("Player 1 turn--> "))
    if player1Input < 0 or player1Input >= totalSize:
        print("Please enter a valid number")
    if len(pickedNumbers) > 0:
        checkMove(player1Input,1)
    playerChoice(player1Input,1)
    printMatrix(matrix)
    if (gameFinishX()):
        print("Winner: X")
        break

    if checkGameFinish():
        break

    #player2
    player2Input = int(input("Player 2 turn--> "))
    if player2Input < 0 or player2Input >= totalSize:
        print("Please enter a valid number")
    if len(pickedNumbers) > 0:
        checkMove(player2Input,2)
    playerChoice(player2Input,2)
    printMatrix(matrix)
    if (gameFinishO()):
        print("Winner: O")
        break

    if checkGameFinish():
        break
