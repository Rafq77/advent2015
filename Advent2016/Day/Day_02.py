﻿fd = open("""../Resources/Day_02.txt""", 'r')
src = fd.read()
fd.close()

keys = src.split('\n')
print(len(keys))

# starting pos is 5
x = 1
y = 1
ops = 0
for seq in keys:
    for char in seq:
        if char == 'R' and x < 2:
            x = x + 1
            #ops = ops + 1
        if char == 'U' and y > 0:
            y = y - 1
            #ops = ops + 1
        if char == 'D' and y < 2:
            y = y + 1
            #ops = ops + 1
        if char == 'L' and x > 0:
            x = x - 1
            #ops = ops + 1
    print("keypos: " + str(x) + "," + str(y))

print("====== task 2 ======")

#task 2
def CheckPos(_x, _y):
    isOk = True;

    if (_x == 0 and _y == 1):
        isOk = False
    if (_x == 1 and _y == 0):
        isOk = False
    if (_x == 0 and _y == 3):
        isOk = False
    if (_x == 1 and _y == 4):
        isOk = False
    if (_x == 3 and _y == 4):
        isOk = False
    if (_x == 4 and _y == 3):
        isOk = False
    if (_x == 4 and _y == 1):
        isOk = False
    if (_x == 3 and _y == 0):
        isOk = False
    if (_x == -1 and _y == 2):
        isOk = False
    if (_x == 2 and _y == -1):
        isOk = False
    if (_x == 5 and _y == 2):
        isOk = False
    if (_x == 2 and _y == 5):
        isOk = False

    return isOk
    
x = 0
y = 2
ops = 0
for seq in keys:
    for char in seq:
        lastX = x
        lastY = y
        if char == 'R':
            x = x + 1
            #ops = ops + 1
        if char == 'U':
            y = y - 1
            #ops = ops + 1
        if char == 'D':
            y = y + 1
            #ops = ops + 1
        if char == 'L':
            x = x - 1
            #ops = ops + 1
        if not CheckPos(x, y):
            x = lastX
            y = lastY
    print("keypos: " + str(x) + "," + str(y)) 
    
