import sys

n=int(sys.stdin.readline())
counseling=[]
dp=[0]*16

for i in range(n):
    counseling.append(list(map(int,sys.stdin.readline().split())))

dp[0]