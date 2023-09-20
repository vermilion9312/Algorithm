t = int(input())

for _ in range(t):
    
    stack = []
    check = True

    ps = input()
    for p in ps:
        if p == '(':
            stack.append(p)
        else:
            if len(stack) > 0:
                stack.pop(-1)
            else:
                check = False
    
    if len(stack) == 0:
        if check:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")