import sys

input = sys.stdin.readline

# 뻔 - 데기 - 뻔 - 데기 - 뻔(n번) - 데기(n번)

A = int(input())
T = int(input())
word = int(input()) # 뻔 : 0 데기 : 1
play_list = []
round = 2

def make_play_list(round) :
    play_list.append(0)
    play_list.append(1)
    play_list.append(0)
    play_list.append(1)

    for _ in range(round) :
        play_list.append(0)

    for _ in range(round) :
        play_list.append(1)

i = 0
Tcount = 0

# 0 1 0 1 0 1 0 1 0 1 0 0 1 1

while True :
    try : 
        if play_list[i] == word :
            Tcount += 1
        if Tcount == T :
            break

        i+=1
    except : 
        make_play_list(round)
        round += 1

print(i%A)