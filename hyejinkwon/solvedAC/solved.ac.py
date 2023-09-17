import sys 

input = sys.stdin.readline

def new_round(n):
    if n-int(n) >= 0.5 :
        return int(n)+1
    else :
        return int(n)

n = int(input())
if n == 0 :
    print(0)
else :
    opinion = []
    for _ in range(n):
        opinion.append(int(input()))

    opinion.sort()
    no_people = new_round(n*0.15)
    if no_people != 0 :
        opinion = opinion[no_people:-no_people]


    print(new_round(sum(opinion)/len(opinion)))