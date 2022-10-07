board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SCFS"

def exist(board,word):
    def explore(x,y,wordIndex):
        if wordIndex >= len(word):
            return True

        board[x][y] = '#'
        possibleSteps = []
        for tempDirection in [[1,0],[-1,0],[0,1],[0,-1]]:
            new_x = x + tempDirection[0]
            new_y = y + tempDirection[1]

            if new_x < 0 or new_x >= len(board):
                continue
            if new_y < 0 or new_y >= len(board[0]):
                continue
            
            if board[new_x][new_y] == word[wordIndex]:
                possibleSteps += [[new_x,new_y]]
        
        if len(possibleSteps) == 0:
            board[x][y] = word[wordIndex-1]
            return False
        else:
            for step in possibleSteps:
                print("origin: (",x,",",y,") ->", step)
                if explore(step[0],step[1],wordIndex+1) == True:
                    return True
            board[x][y] = word[wordIndex-1]
            return False


    # check is all word exist
    wordDic = {}
    for row in board:
        for letter in row:
            if letter in wordDic:
                wordDic[letter] += 1
            else:
                wordDic[letter] = 1
    for letter in list(set(word)):
        if letter not in wordDic:
            return False
        else:
            if word.count(letter) > wordDic[letter]:
                return False

    startPoints = []
    for row in range(len(board)):
        for column in range(len(board[0])):
            if board[row][column] == word[0]:
                startPoints += [[row,column]]
    if len(startPoints) == 0:
        return False
    else:
        for pairs in startPoints:
            print(pairs)
            print(board)
            if explore(pairs[0],pairs[1],1) == True:
                return True
        
        return False

print("final ==> ", exist(board,word))