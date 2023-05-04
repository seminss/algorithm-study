import sys

input = sys.stdin.readline
N = int(input())
string_list = []
for _ in range(N) :
    string_list.append(input().strip())
string_list = list(set(string_list))
string_list.sort()
string_list = sorted(string_list, key=lambda x: len(x))

for s in string_list:
    print(s)