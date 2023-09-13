s = input()

y = "YONSEI"
k = "KOREA"

for i in range(len(s)):
    if s[i] == y[0]:
        y = y[1:]
    if s[i] == k[0]:
        k = k[1:]
    
    if len(k) == 0:
        print("KOREA")
        break
    if len(y) == 0:
        print("YONSEI")
        break