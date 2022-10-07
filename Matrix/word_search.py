board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "WEEEEE"
directions = [[1,0],[-1,0],[0,1],[0,-1]]

def exist(board,word):
    def explore(x,y,wordIndex, visited):
        if wordIndex >= len(word):
            return True
        
        sub_visited = []
        for i in board:
            sub_visited += [[0]*len(board[0])]
        for i in range(len(board)):
            for j in range(len(board[0])):
                sub_visited[i][j] = visited[i][j]
        sub_visited[x][y] = 1

        possibleSteps = []
        for tempDirection in directions:
            new_x = x + tempDirection[0]
            new_y = y + tempDirection[1]

            if new_x < 0 or new_x >= len(board):
                continue
            if new_y < 0 or new_y >= len(board[0]):
                continue
            if sub_visited[new_x][new_y] == 1:
                continue
            
            if board[new_x][new_y] == word[wordIndex]:
                possibleSteps += [[new_x,new_y]]
        
        if len(possibleSteps) == 0:
            return False
        else:
            # copy matrix
            for step in possibleSteps:
                print("origin: (",x,",",y,") ->", step)
                if explore(step[0],step[1],wordIndex+1,sub_visited) == True:
                    return True
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
            visited = []
            for i in board:
                visited += [[0]*len(board[0])]
            if explore(pairs[0],pairs[1],1,visited) == True:
                return True
        
        return False

print("final ==> ", exist(board,word))