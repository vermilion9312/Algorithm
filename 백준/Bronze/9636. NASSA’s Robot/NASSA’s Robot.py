n = int(input())

posX = 0
posY = 0
delta = 0

for _ in range(n):
    movement = input()
    for i in range(len(movement)):
        if movement[i] == 'R':
            posX += 1
        if movement[i] == 'L':
            posX -= 1
        if movement[i] == 'U':
            posY += 1
        if movement[i] == 'D':
            posY -= 1
        if movement[i] == '?':
            delta += 1

    print(posX - delta, posY - delta, posX + delta, posY + delta)
    posX = 0
    posY = 0
    delta = 0