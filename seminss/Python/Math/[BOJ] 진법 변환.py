import sys

n,b=map(str,sys.stdin.readline().split())
result=0

def convert(num,i):
    return num*(int(b)**i)

for i in range(len(n)):
    a=n[len(n)-i-1]
    if a.isdigit():
        result+=convert(int(a),i)
    else:
        result+=convert(ord(a)-65+10,i) #'A'의 아스키 코드는 65

print(result)
