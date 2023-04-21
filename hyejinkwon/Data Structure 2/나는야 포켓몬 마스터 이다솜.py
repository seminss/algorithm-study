import sys

input = sys.stdin.readline

N, M = map(int , input().split())
dict_pocketmon = {}

for i in range(1,N+1) :
    pocketmon = input().rstrip()
    dict_pocketmon[pocketmon] = i
    dict_pocketmon[i] = pocketmon

for j in range(M) :
    pocketmon_input = input().rstrip()
    if pocketmon_input.isdigit() :
        print(dict_pocketmon[int(pocketmon_input)])
    else :
        print(dict_pocketmon[pocketmon_input])