import sys 

input = sys.stdin.readline

coin = int(input())
coin_count = 0

while coin != 0 :
    if coin % 5 == 0:
        coin_count += coin//5
        break  
    else :
        coin -= 2
        coin_count += 1

    if coin <0 :
        break

if coin < 0 : 
    print(-1)
else :
    print(coin_count)

