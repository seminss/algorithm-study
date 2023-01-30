import sys
pm_arr=[] # +,- 저장하는 list
stack=[] # stack

N=int(sys.stdin.readline())
last_input=0

for i in range(N):
    # 오름차순 push이므로 순차적으로 한번만 push하면 됨.
    num=int(sys.stdin.readline())

    for j in range(last_input+1,num+1):
        stack.append(j)
        pm_arr.append("+")
        last_input=num
    
    # pop은 입력받은 num까지 append를 마친 뒤에,
    # 최종적으로 stack의 top값과 num 값이 일치하면 해주면 된다.
    if stack[-1]==num:
        stack.pop()
        pm_arr.append("-")

# 정상적으로 수열이 생성됐다면, pop이 끝까지 되어 stack은 비워져 있어야 함
if len(stack)!=0:
    print("NO")
else:
    for i in pm_arr:
        print(i)
