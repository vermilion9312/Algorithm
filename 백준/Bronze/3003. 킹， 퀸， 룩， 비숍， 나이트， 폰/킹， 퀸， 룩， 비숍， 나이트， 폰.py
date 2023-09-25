pieces = [1, 1, 2, 2, 2, 8]
foundPieces = list(map(int, input().split()))

for i in range(len(pieces)):
    pieces[i] -= foundPieces[i]

print(*pieces)