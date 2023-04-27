# https://www.acmicpc.net/problem/25501

print("230428-5-0324")

def recursion(s, l, r):
    if l >= r:
        return '1 ' + str(l + 1)
    elif s[l] != s[r]:
        return '0 ' + str(l + 1)
    else:
        return recursion(s, l + 1, r - 1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

t = int(input())

for _ in range(t):
    s = input()
    print(isPalindrome(s))