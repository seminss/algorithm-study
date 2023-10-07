import sys

switchCount = int(sys.stdin.readline())
switches = list(map(int, sys.stdin.readline().split()))
stuCount = int(sys.stdin.readline())

def switch(n):
    if switches[n - 1] == 1:
        switches[n - 1] = 0
    else:
        switches[n - 1] = 1

def boy(switchNum):
    targetNum = switchNum
    while targetNum <= switchCount:
        switch(targetNum)
        targetNum += switchNum

def girl(switchNum):
    width = 0
    while switchNum - (width + 1) - 1 >= 0 and switchNum + (width + 1) - 1 < switchCount:
        if switches[switchNum - (width + 1) - 1] == switches[switchNum + (width + 1) - 1]:
            width += 1
        else:
            break

    for i in range(switchNum - width, switchNum + width + 1):
        switch(i)

switchFunc = [0, boy, girl]
for _ in range(stuCount):
    gender, switchNum = map(int, sys.stdin.readline().split())
    switchFunc[gender](switchNum)

while switches:
    print(*switches[:20])
    switches = switches[20:]