w, h = 4, 4
map = [['.' for x in range(w)] for y in range(h)] 

px, py = 1, 1
bx, by = 2, 2
sx, sy = 3, 2

def printMap():
    nums = [0,1,2,3]
    for count in nums:
        print(map[count])
    return
def updateMap():
    nums = [0,1,2,3]
    for count1 in nums:
        for count2 in nums:
            map[count1][count2] = '.';
    map[px][py] = 'P';
    map[bx][by] = 'B';
    map[sx][sy] = 'S';
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
    global bx, by
    if move=='w':
        bx-=1
    elif move=='a':
        by-=1
    elif move=='s':
        bx+=1
    elif move=='d':
        by+=1
    return
def isBoxMoved(px, py, bx, by, move):
    if (bx-px)==0 and by==py and move=='s':
        return 1
    elif (by-py)==0 and bx==px and move=='d':
        return 1
    elif (px-bx)==0 and by==py and move=='w':
        return 1
    elif (py-by)==0 and bx==px and move=='a':
        return 1
    else: 
        return 0
def isValidMove(px, py, move):
    if px==0 and move=='w':
        return 0
    elif py==0 and move=='a':
        return 0
    elif px==3 and move=='s':
        return 0
    elif py==3 and move=='d':
        return 0
    else:
        return 1
def winGame(bx, by, sx, sy):
    if bx==sx and by==sy:
        return 1
    else:
        return 0
def isGameOver():
    if bx==0 and by==0:
        return 1
    elif bx==0 and by==3:
        return 1
    elif bx==3 and by==0:
        return 1
    elif bx==3 and by==3:
        return 1
    else:
        return 0
    
while not(isGameOver()):
    updateMap()
    printMap()
    move = input("Your next move : ")
    if isValidMove(px, py, move):
        movePlayer(move)
    else:
        print('Not valid move!')
        continue
    if isBoxMoved(px, py, bx, by, move):
        moveBox(move)
        if winGame(bx, by, sx, sy):
            map[bx][by]='B'
            printMap()
            print('YOU WIN!!!')
            break
        if isGameOver():
            printMap()
            print('GAME OVER!')
            break
print('Thank you for playing')