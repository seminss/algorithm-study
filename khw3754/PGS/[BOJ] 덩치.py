n = int(input())
people = []
for _ in range(n):
    a, b = map(int, input().split())
    people.append((a, b))

for i in range(n):
    count = 0
    for j in range(n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            count += 1
    print(count+1)