dice1, dice2, dice3 = map(int, input().split())

if dice1 == dice2 == dice3:
    reward = 10000 + dice1 * 1000

elif dice1 == dice2:
    reward = 1000 + dice1 * 100

elif dice2 == dice3:
    reward = 1000 + dice2 * 100

elif dice1 == dice3:
    reward = 1000 + dice1 * 100

else:
    reward = max(dice1, dice2, dice3) * 100

print(reward)