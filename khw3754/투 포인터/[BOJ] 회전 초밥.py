from collections import deque
import sys

N, d, k, c = map(int, input().split())

sushis = deque()
for _ in range(N):
    sushis.append(int(sys.stdin.readline()))

count = 0
result = 0
sushi_count = {i:0 for i in range(1, d+1)}

# 초기화 (처음부터 쿠폰 스시는 넣고 계산)
sushi_count[c] += 1
count += 1

for _ in range(k):
    s = sushis.popleft()
    if sushi_count[s] == 0:
        count += 1
    sushi_count[s] += 1
    sushis.append(s)

result = count


# 투 포인터로 탐색
for _ in range(N-1):
    sta = sushis[-k]
    sushi_count[sta] -= 1
    if sushi_count[sta] == 0:
        count -= 1

    s = sushis.popleft()
    if sushi_count[s] == 0:
        count += 1
    sushi_count[s] += 1
    sushis.append(s)

    if result < count:
        result = count
    if result == k + 1:
        break

print(result)

# print(sushi_count)
# print(save_count)
# print(sushis)