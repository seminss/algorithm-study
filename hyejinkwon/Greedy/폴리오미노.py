import sys 

input = sys.stdin.readline
board = input().rstrip()
# AAAA BB 무조건 짝수 형태

answer = board.replace("XXXX","AAAA")
answer = answer.replace("XX","BB")

if "X" in answer :
    print(-1)
else :
    print(answer)

