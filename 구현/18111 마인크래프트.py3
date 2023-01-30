import sys
n,v,b=map(int,sys.stdin.readline().split())

house=[]
for i in range(n):
    house.append(list(map(int,sys.stdin.readline().split()))) #2차원 배열
house=sum(house,[]) #1차원 배열로 만들기

house.sort(reverse=True)
low=min(house)
high=max(house)
#low<=고른높이<=max
#각 원소가 높이와 다르면 제거 or 올리기
result_time=500*500*256
result_height=0
# print(house)

for h in range(low,high+1,1):
    tmp=house.copy()
    time=0
    iventory=b
    stop=False
    # print("시작",h,time,iventory)
    for e in range(n*v):
        if tmp[e]>h:
            #뺄 때는 빼고 인벤토리에 넣기, 2초
            # print(e,":",tmp[e],"-",h)
            iventory+=tmp[e]-h
            time=time+2*(tmp[e]-h)
            tmp[e]=h
        elif tmp[e]<h:
            #쌓을 때는 인벤토리에 있는지 확인하고 쌓기, 1초
            # print(e,":",tmp[e],"+",h)
            if iventory>=h-tmp[e]:
                iventory-=h-tmp[e]
                time=time+1*(h-tmp[e])
                tmp[e]=h
                #내림차순으로 정렬을 해뒀기 때문에 낮은 쪽 채울 때 인벤토리에 없으면 그 높이는 안되는 거임
        if iventory<0:
            break
        #같은 건 pass하면 됨
        # print("done",h,time,iventory,tmp)
        # print("time,h,inventory",time,h,iventory,tmp)
    if tmp[0]==tmp[-1] and time<=result_time and time!=0:
        result_time=time
        result_height=h
if result_time==500*500*256:
    result_height=house[0]
    result_time=0
print(result_time,result_height)