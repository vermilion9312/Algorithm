while True:
    try:
        position = list(map(int, input().split()))
        distance1 = abs(position[0] - position[1])
        distance2 = abs(position[1] - position[2])
        if distance1 < distance2:
            print(distance2 - 1)
        else:
            print(distance1 - 1)
    except:
        break