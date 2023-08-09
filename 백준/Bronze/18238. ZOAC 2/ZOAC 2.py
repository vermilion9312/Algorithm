strAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
intRefDistance = len(strAlphabet) // 2 # 최단 시간을 판별하는 기준 시간, 한 바퀴 돌리는데 걸리는 시간의 반절이다

strInput = input() # 예시 입력으로 'ZOAC'을 받는다
intCntIdx = 0 # 처음 시작하는 글자는 A이므로 현재 인덱스는 0이다
intCount = 0 # 출력할 결과값 초기값 설정

for strLetter in strInput: # Z, O, A, C 순으로 돌아간다

    intNxtIdx = strAlphabet.find(strLetter) # 다음 인덱스를 구한다
    intIdxDiff = abs(intNxtIdx - intCntIdx) # 현재 인덱스에서 다음 인덱스까지 걸리는 시간을 구한다
    
    if intIdxDiff <= intRefDistance: # 기준 시간이 넘어가지 않으면 최단시간이므로
        intCount += intIdxDiff # 그냥 결과값에 더해준다
    else: # 기준을 넘어가면
        intCount += (len(strAlphabet) - intIdxDiff) # 전체에서 기준 시간을 넘어가는 시간을 빼준다

    intCntIdx = intNxtIdx # 다음 인덱스는 현재 인덱스가 된다

print(intCount) # 결과값 출력