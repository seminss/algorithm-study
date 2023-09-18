import sys 

input = sys.stdin.readline
ss = input().rstrip()
ss = ss.split("-")
s_minus = []

for s in ss :
    sum_value = 0
    s_plus = s.split("-")
    for s_p in s_plus :
        sum_value -= int(s_p)

    s_minus.append(sum_value)

answer = s_minus[0]
for i in range(1, len(s_minus)) :
    answer += s_minus[i]
print(answer)
    
