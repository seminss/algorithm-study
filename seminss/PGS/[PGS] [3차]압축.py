dic = {chr(i + 65): i + 1 for i in range(26)}
def solution(msg):
    answer = []
    d_idx = 27
    head,tail=0,1
    # if len(msg) == 1:
    #     return dic[msg]
    while tail<len(msg)+1:
        if msg[head:tail] in dic:
            tail += 1
        else:
            dic[msg[head:tail]] = d_idx
            d_idx += 1
            answer.append(dic[msg[head:tail-1]])
            head,tail=tail-1,tail
    answer.append(dic[msg[head:tail-1]])
    return answer

#굳이 안해도 되기는 하지만 처음에 문자열 길이가 1일때 예외처리를 해줬는데, 하면 95점이 나오네욥..
#뭐가 문젠지 모르겠어용