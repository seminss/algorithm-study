''' 2023.5.10
17:05 ~ 17:25
23:48 ~ 23:58
'''

# n <= 5*10^6
n = int(input())
cards = list(map(int, input().split(' ')))
# n <= 5*10^6
m = int(input())
targets = list(map(int, input().split(' ')))

# dictionary 초기화
d = dict()
for card in cards:
    if card in d:
        d[card] += 1
    else:
        d[card] = 1

# 이분 탐색
cards.sort()
answer = []
for x in targets:
    '''
    # binary search
    left, right, mid = 0, cards[-1], 0
    while left <= right:
        mid = (left+right)//2
        if mid == x:
            answer.append(d[x])
        elif mid < x:
            left = mid + 1
        else:
            right = mid - 1
    '''
    if x in d:
        print(d[x], end=' ')
    else:
        print(0, end=' ')
