import sys

input = sys.stdin.readline
M = int(input())
S = set()

for _ in range(M) :
    command = input().rstrip()
    if ' ' in command :
        command, x = command.split()
        print("x : ",x)
        x = int(x) 

    if command == "add" : S.add(x)
    elif command == "remove" and x in S : S.remove(x)
    elif command == "check" :
        if x in S : print(1)
        else : print(0)
    elif command == "toggle" :
        if x in S : S.remove(x)
        else : S.add(x)
    elif command == "all" : S = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif command == "empty" : S = set()