import sys

input = sys.stdin.readline
test_case = []
test_case.append(sorted(list(map(int, input().split()))))

while True :
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0 :
        break
    else :
        test_case.append(sorted([a,b,c]))

for a,b,c in test_case :
    if c**2 == a**2 + b**2 :
        print("right")
    else :
        print("wrong")