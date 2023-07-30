townNum = int(input()) # 마을의 수
expenseList = list(map(int, input().split())) # 이동비용 리스트
minExpense = sum(expenseList) - max(expenseList)
print(minExpense)