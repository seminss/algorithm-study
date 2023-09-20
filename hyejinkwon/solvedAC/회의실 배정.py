import sys
input = sys.stdin.readline

# 회의 끝나는 시간 -> 회의 시작시간 정렬

N = int(input())

meeting = []
for i in range(N):
    meeting.append(list(map(int, input().split())))    

meeting.sort(key = lambda x: (x[1], x[0]))
room = 1
end_time = meeting[0][1]
for i in range(1, N) :
    if meeting[i][0] >= end_time:
        room += 1
        end_time = meeting[i][1]

print(room)