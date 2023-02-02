#백준 10825

import sys
input=sys.stdin.readline

n=int(input().strip())

#2차원 배열 입력받기
student=[0 for _ in range(n)]
for i in range(n):
    student[i]=list(map(str,input().split()))

#국,영,수,이름 순이기 때문에 이름을 리스트 마지막으로
for i in range(n):
    student[i].append(student[i].pop(0))

#lamda로 조건 줘서 sort
#정수의 경우에는 음수로 변환하여 reverse sort 편하게 가능
student.sort(key=lambda student:(-int(student[0]),int(student[1]),-int(student[2]),student[3]))

for i in range(n):
    print(student[i][3])

