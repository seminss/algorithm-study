#20m

import sys

s=int(sys.stdin.readline())
sm=0
cnt=0
if s==1:
    print(1)
for i in range(1,round(s/2)+2):
    sm+=i
    cnt+=1
    if sm>s:
        print(cnt-1)   
        break 

# 1->1
# 2->2
# 3->1,2
# 4->1,3
# 5->2,3/1,4
# 6->1,2,3
# 7->1,2,4
# 8->1,2,3,4