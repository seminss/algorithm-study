# 백준 18310

import sys
input=sys.stdin.readline

n=int(input())
house=list(map(int,input().split()))
house.sort()
length=(len(house)-1)//2 

print(house[length]) #중앙값 구하기