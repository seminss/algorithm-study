import sys

input = sys.stdin.readline

N,r,c = map(int,input().split())
answer = 0 

while N != 0 :
    N -= 1
    size = 2**N

    if r < size and c < size :
        answer += 0
    elif r < size and c >= size :
        answer += size*size
        c -= size
    elif r >= size and c < size :
        answer += size*size*2
        r -= size
    elif r >= size and c >= size :
        answer += size*size*3
        r -= size
        c -= size
print(answer)