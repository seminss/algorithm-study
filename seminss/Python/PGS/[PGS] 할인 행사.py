def solution(want, number, discount):
    dic={want[i]:number[i] for i in range(len(want))}
    answer=0
    for i in range(len(discount)-9):
        possible=0
        for k,v in dic.items():
            if v!=discount[i:i+10].count(k):
                break
            else:
                possible+=1
        if possible==len(dic):
            answer+=1
    return answer