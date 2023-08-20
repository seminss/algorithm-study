from itertools import combinations as combi
from itertools import permutations as permu


# 모든 경우의 수를 탐색
def solution(k, dungeons):
    answer = 0

    dungeons = list(filter(lambda x: x[0] <= k, dungeons))

    # 모든 경우의 수에 대해 시뮬
    for i in range(1, len(dungeons) + 1)[::-1]:
        for com in combi(dungeons, i):
            for per in permu(com):
                # 가능한지 검사
                kk = k
                for dungeon in per:
                    # 탐험할 수 없으면 break
                    if dungeon[0] > kk:
                        break
                    # 있으면 진행
                    else:
                        kk -= dungeon[1]
                # 탐험가능하면 즉시 return
                else:
                    return i

    return answer