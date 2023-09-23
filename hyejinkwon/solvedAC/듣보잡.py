import sys

input = sys.stdin.readline
N,M = map(int,input().split())
listen = set()
watch = set()

for _ in range(N) :
    listen.add(input().rstrip())
for _ in range(M) :
    watch.add(input().rstrip())

listen_watch = sorted(list(listen&watch))

print(len(listen_watch))
for lw in listen_watch:
    print(lw)