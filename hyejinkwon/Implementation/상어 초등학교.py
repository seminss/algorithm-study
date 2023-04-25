import sys

# r행 c열
# 한칸에 한 학생
# |r1 - r2| + |c1 - c2| = 1 인접
# 인접한 학생 수
# 1: 1점, 2 : 10점, 3: 100점, 4 : 1000점

input = sys.stdin.readline
N = int(input())
class_seat = [ [0]*(N+1)  for _ in range(N+1) ]
# 오 왼 아래 위
dx = [0,0,1,-1]
dy = [1,-1,0,0]

like_student_list = []

for _ in range(N**2) :
    input_content = list(map(int, input().split()))
    now = input_content[0]
    now_like = input_content[1:]
    like_student_list.append(input_content)
    choice_list = []

    for i in range(1,N+1) :
        for j in range(1, N+1) :
            if class_seat[i][j] == 0 : # 아무도 앉지 않았다면
                adjoin_like = 0
                empty = 0
                for k in range(4) :
                    xx = i + dx[k]
                    yy = j + dy[k]

                    if 1<=xx<=N and 1 <=yy<=N :
                        if class_seat[xx][yy] in now_like :
                            adjoin_like += 1

                        if class_seat[xx][yy] == 0 :
                            empty += 1
                
                choice_list.append([adjoin_like, empty, i,j])

    choice_list = sorted(choice_list, key = lambda x : (-x[0], -x[1], x[2], x[3]))
    class_seat[choice_list[0][2]][choice_list[0][3]] = now

like_student_list.sort()

sum = 0 
for i in range(1,N+1) :
    for j in range(1,N+1) :
        count = 0 
        
        for k in range(4) :
            xx = i + dx[k]
            yy = j + dy[k]

            if 1<=xx<=N and 1<=yy<=N :
                if class_seat[xx][yy] in like_student_list[class_seat[xx][yy]-1] : 
                    count += 1

        if count != 0 :
            sum += 10**(count-1)

print(sum)

            
                    


