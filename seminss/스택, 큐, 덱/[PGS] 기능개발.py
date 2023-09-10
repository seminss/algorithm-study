import math
def solution(progresses, speeds):
    answer = []
    days=[0]*len(progresses)
    for i in range(len(days)): #각 기능들별로 몇일 씩 걸리는지 계산
        days[i]=math.ceil((100-progresses[i])/speeds[i])

    div=days[0] #기준 기간
    each=1 #한 번에 배포될 작업 수
    for j in range(1,len(days)):
        if days[j]>div: #더 긴 기간을 만나기 전까지는 앞선 작업이 배포될 때 같이 배포된다.
            answer.append(each)
            div=days[j] #갱신
            each=1
        else:
            each+=1
        if j==len(days)-1:
            answer.append(each) #끝에 도달하면 그냥 지금까지 쌓인거 append
    return answer