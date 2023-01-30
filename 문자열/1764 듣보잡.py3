import sys

n,m=map(int,sys.stdin.readline().split())
name_list={}

for i in range(n):
    name=sys.stdin.readline().strip() 
    name_list[name]=1

for j in range(m):
    name=sys.stdin.readline().strip()
    if name in name_list:
        name_list[name]+=1

result=list(filter(lambda item:item[1]==2,name_list.items()))

print(len(result))
for name,cnt in sorted(result):
    print(name)