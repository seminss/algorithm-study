import sys
N=int(sys.stdin.readline())
six=666

while N: #N은 666을 포함할 때만 준다. N=0 되면 종료
    if "666" in str(six):
        N-=1
    six+=1
print(six-1)