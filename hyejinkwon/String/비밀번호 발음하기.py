import sys

input = sys.stdin.readline

vows = "aeiou"

while True:
    s = input().rstrip()
    if s == "end":
        break
    check1 = False
    check2 = True
    for i in range(len(s)):
        if s[i] in vows:
            check1 = True
        if i > 0:
            if s[i] == s[i-1] and s[i] != 'e' and s[i] != 'o':
                check2 = False
                break
        if i > 1:
            if s[i] not in vows:
                if s[i-1] not in vows:
                    if s[i-2] not in vows:
                        check2 = False
                        break
            if s[i] in vows:
                if s[i-1] in vows:
                    if s[i-2] in vows:
                        check2 = False
                        break
    if check1 and check2:
        print("<" + s + "> is acceptable.")
    else:
        print("<" + s + "> is not acceptable.")