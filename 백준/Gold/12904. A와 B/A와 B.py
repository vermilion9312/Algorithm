s = input()
t = input()

while True:
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]

    if len(s) == len(t) and s == t:
        print(1)
        break
    if len(s) == len(t) and s != t:
        print(0)
        break