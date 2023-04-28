# https://www.acmicpc.net/problem/17478

print("230428-5-0922")

n = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

question = "\"재귀함수가 뭔가요?\"\n"

loopAnswer1 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n"
loopAnswer2 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n"
loopAnswer3 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n"

underscore = "____"

rearString = "라고 답변하였지.\n"

lastAnswer = "\"재귀함수는 자기 자신을 호출하는 함수라네\"\n"

script = ""
def loop(i, n):
    if n == 0:
        return i * underscore + question + i * underscore + lastAnswer + i * underscore + rearString
        
    else:
        return i * underscore + question + i * underscore + loopAnswer1 + i * underscore + loopAnswer2 + i * underscore + loopAnswer3 + loop(i + 1, n - 1)  + i * underscore + rearString

print(loop(0, n))