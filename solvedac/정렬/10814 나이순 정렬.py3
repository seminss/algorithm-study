import sys
N=int(sys.stdin.readline())
p_list=[0 for i in range(N)]
for i in range(N):
    old,name=map(str,sys.stdin.readline().split())
    p_list[i]=(int(old),i,name)

p_list.sort()
for old,idx,name in p_list:
    print(old, name)