import sys

input = sys.stdin.readline

N, X = map(int, input().split())
visited = list(map(int,input().split()))

# [:X] 만큼 더해서 최대값구하기
# N-X+1개만큼의 조합가능
# Sliding Window
    