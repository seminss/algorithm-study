# 4:57~5:30
from itertools import permutations
from itertools import combinations

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]
people = [i for i in range(n)]
result = 100 * 20

for start in combinations(people, n // 2):
    start = list(start)
    link = [x for x in people if x not in start]

    start_sum = 0
    for s in permutations(start, 2):
        start_sum += maps[s[1]][s[0]]

    link_sum = 0
    for l in permutations(link, 2):
        link_sum += maps[l[1]][l[0]]

    result = min(abs(start_sum - link_sum), result)
    if result == 0:
        break

print(result)
