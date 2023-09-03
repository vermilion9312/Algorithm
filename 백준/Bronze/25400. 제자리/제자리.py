cardCount = int(input())
cardList = list(map(int, input().split()))

sortedCardList = []
cardIdx = 1

for card in cardList:
    if card == cardIdx:
        sortedCardList.append(card)
        cardIdx += 1

print(cardCount - len(sortedCardList))