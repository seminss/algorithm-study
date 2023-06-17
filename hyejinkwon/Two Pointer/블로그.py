import sys

input = sys.stdin.readline

N, X = map(int, input().split())
visited = list(map(int,input().split()))
answer = [sum(visited[0:X])]
value = answer[0]

if max(visited) == 0 :
    print("SAD")
    exit(0)

for i in range(X,N) :
    value += visited[i]
    value -= visited[i-X]
    answer.append(value)

answer = sorted(answer, reverse=True)
max_people = answer[0]
day = 1

for i in range(1, len(answer)) :
    if max_people == answer[i] :
        day += 1
    else :
        break

print(max_people)
print(day)
