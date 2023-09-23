import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T) :
    floor = int(input())
    num = int(input()) 
    house = [i for i in range(1,num+1)]

    for k in range(floor):
        for j in range(1,num) :
            house[j] += house[j-1]

    print(house[-1])