import sys
input = sys.stdin.readline
# 1234567
N,K =map(int,input().split())
per = [ i for i in range(1,N+1)]
answer = []
index = 0
while per != [] :
    index += K -1
    if len(per) <= index :
        index %= len(per)
    answer.append(per[index])
    per.remove(per[index])

result = "<"
for a in answer :
    result += str(a) + ", "

result = result[:-2]
result += ">"
print(result)