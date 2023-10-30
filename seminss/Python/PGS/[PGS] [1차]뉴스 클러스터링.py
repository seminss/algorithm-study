import math
def solution(str1, str2):
    inter,union=[],[]
    str1,str2=str1.lower(), str2.lower()
    set1=[str1[i:i+2] for i in range(0,len(str1),1) if len(str1[i:i+2])==2 and str1[i:i+2].isalpha()]
    set2=[str2[i:i+2] for i in range(0,len(str2),1) if len(str2[i:i+2])==2 and str2[i:i+2].isalpha()]
    for s1 in set1:
        union.append(s1)
        if s1 in set2:
            inter.append(s1)
            set2.remove(s1)
    for s2 in set2:
        union.append(s2)
    if len(union):
        answer=math.floor((len(inter)/len(union)*65536))
    else:
        answer=65536
    return answer

# 처음에는 공집합을 처리하는 부분의 조건을 len(union) and len(inter) 로 했다.
# 반례로, solution("aa1+aa2", "AAAA12") 이 존재하며, 이런 경우는 합집합은 있지만, 교집합이 0인 경우다. 
# 이 때 65536이 아니라 0이 되어야 한다. -> len(union) 으로 수정해 나눗셈이 불가능한 경우만 잡게끔 했다.