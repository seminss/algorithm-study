# 각 기능은 진도가 100%일 때 서비스에 반영 가능
# progresses

def solution(progresses, speeds):
    answer = []
    day = []
    
    for i,p in enumerate(progresses) :
        if (100-p) % speeds[i] == 0 :
            day.append((100-p)//speeds[i])
        else :
            day.append((100-p)//speeds[i] + 1)
            
    before_d = day[0]
    distribution = 0

    for d in day :
        if before_d < d :
            answer.append(distribution)
            distribution = 1
            before_d = d
        else :
            distribution += 1
            
    answer.append(distribution)
    return answer