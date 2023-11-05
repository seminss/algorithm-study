def solution(s):
    answer = []
    data=s[2:-2].split('},{')
    data.sort(key=lambda x : len(x))
    for i in data:
        for j in i.split(','):
            if int(j) not in answer:
                answer.append(int(j))
    return answer
    