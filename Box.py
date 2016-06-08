w, h = 5, 5
map = [['.' for x in range(w)] for y in range(h)] 
box = [[0 for x in range(w)] for y in range(h)]
store = [[0 for x in range(w)] for y in range(h)]

px, py = 1, 1
box[1][3] = box[3][1] = 1
store[4][1] = store[4][3] = 1


def printMap():
    nums = [0,1,2,3,4]
    for count in nums:
        print(map[count])
    return
def updateMap():
    nums = [0,1,2,3,4]
    for count1 in nums:
        for count2 in nums:
            if box[count1][count2]==1:
                map[count1][count2] = 'B'
            elif store[count1][count2]==1:
                map[count1][count2] = 'S'
            else:
                map[count1][count2] = '.';
    map[px][py] = 'P';
    return
def movePlayer(move):
    global px, py
    if move=='w':
        px-=1
    elif move=='a':
        py-=1
    elif move=='s':
        px+=1
    elif move=='d':
        py+=1
    return
def moveBox(move):
    global box
    global px, py
    if move=='w':
        box[px][py] = 0
        box[px-1][py] = 1
    elif move=='a':
        box[px][py] = 0
        box[px][py-1] = 1
    elif move=='s':
        box[px][py] = 0
        box[px+1][py] = 1
    elif move=='d':
        box[px][py] = 0
        box[px][py+1] = 1
    return
def isBoxMoved(px, py, move):
        if box[px][py]==1:
            return 1
        else: 
            return 0
def isValidMove(px, py, move):
    if px==0 and move=='w':
        return 0
    elif py==0 and move=='a':
        return 0
    elif px==4 and move=='s':
        return 0
    elif py==4 and move=='d':
        return 0
    else:
        return 1
def checkBoxStored():
    global box
    global store
    for count1 in range(5):
        for count2 in range(5):
            if box[count1][count2]==1 and store[count1][count2]==1:
                store[count1][count2] = 0
    return
def winGame():
    global box
    for count1 in range(5):
        for count2 in range(5):
            if store[count1][count2]==1:
                return 0
    return 1
def isGameOver():
    if box[0][0]==1 or box[0][4]==1 or box[4][0]==1 or box[4][4]==1:
        return 1
    else:
        return 0
    
while not(isGameOver()):
    updateMap()
    printMap7
    move = input("Your next move : ")
    if isValidMove(px, py, move):
        movePlayer(move)
    else:
        print('Not valid move!')
        continue
    if isBoxMoved(px, py, move):
        moveBox(move)
        checkBoxStored()
        if winGame():
            updateMap()
            printMap()
            print('YOU WIN!!!')
            break
        if isGameOver():
            printMap()
            print('GAME OVER!')
            break
print('Thank you for playing')