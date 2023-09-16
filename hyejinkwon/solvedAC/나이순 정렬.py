import sys

input = sys.stdin.readline

N = int(input())
member = []
for _ in range(N) :
    age, name = input().split()
    age = int(age)
    member.append([age,name])

member = sorted(member, key=lambda x : x[0])

for age,name in member :
    print(age,name)