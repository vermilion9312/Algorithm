seatCount = int(input())
seatStr = input()

coupleSeatCount = 0

for seat in seatStr:
    if seat == 'L':
        coupleSeatCount += 1

coupleSeatCount //= 2

if coupleSeatCount > 0:
    coupleSeatCount -= 1

resultCount = seatCount - coupleSeatCount
print(resultCount)