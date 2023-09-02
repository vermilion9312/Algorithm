n, l, k = map(int, input().split())

userScore = 0
sub1Score = 100
sub2Score = 140
sub1Count = 0
sub2Count = 0

for _ in range(n):
    sub1, sub2 = map(int, input().split())
    if sub2 <= l:
        sub2Count += 1
    elif sub1 <= l:
        sub1Count += 1

if sub2Count >= k:
    userScore += k * sub2Score
else:
    userScore += sub2Count * sub2Score
    k -= sub2Count
    
    if sub1Count < k:
        userScore += sub1Count * sub1Score
    else:
        userScore += k * sub1Score

print(userScore)