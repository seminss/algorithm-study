import sys
input = sys.stdin.readline

N = int(input())

'''
어떤 수에 6이 적어도 3개 이상 연속으로 들어가는 수
'''
end = 666
while N :
    if "666" in str(end) :
        N -=1
    end +=1
        
print(end-1)