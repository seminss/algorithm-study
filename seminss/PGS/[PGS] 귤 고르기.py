def solution(k, tangerine):
    answer=0
    tan_dic={}
    
    for t in tangerine:
        if t not in tan_dic:
            tan_dic[t]=1
        else:
            tan_dic[t]+=1

    tan_dic=sorted(tan_dic.items(),key=lambda x:x[1], reverse=True)
    
    for key,value in tan_dic:
        if k <= 0: 
            break
        k -= value
        answer += 1
        
    return answer

# from collections import Counter을 해서 아래와 같이 딕셔너리를 초기화+정렬 하는 방법도 있습니다.
# count = sorted(Counter(tangerine).items(),reverse = True, key = lambda x : x[1])
# 처음에 배열 인덱스에 개수를 저장했는데, 그러면 런타임 에러가 납니다.