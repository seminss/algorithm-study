# 2023.6.30
# 16:45 ~ 17:05
n, x = map(int, input().split(' '))
visitor = list(map(int, input().split(' ')))

d1, d2 = 0, 0
tmp = visitor[0] # d1 ~ d2 까지의 방문자 수
answer = [0, 0] # 최대 방문자 수, 기간 개수

while d1 <= n - x:
    # x일동안의 방문자 수를 구한다.
    while d2 - d1 + 1 < x:
        d2 += 1
        tmp += visitor[d2]
    # 기간 개수 추가
    if answer[0] == tmp and tmp > 0:
        answer[1] += 1
    # 최대 방문자 수 업데이트
    elif answer[0] < tmp:
        answer[0] = tmp
        answer[1] = 1
    d1 += 1
    tmp -= visitor[d1-1]
    # print(f'd1: {d1} d2: {d2} answer: {answer[0]} tmp: {tmp}')

if answer[0] == 0:
    print('SAD')
else:
    print(answer[0])
    print(answer[1])
