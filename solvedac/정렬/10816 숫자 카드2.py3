import sys
n = sys.stdin.readline()
hav_card = map(int,sys.stdin.readline().split())
m = sys.stdin.readline()
find_card = map(int,sys.stdin.readline().split())

hashmap = {}
for n in hav_card:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in find_card))