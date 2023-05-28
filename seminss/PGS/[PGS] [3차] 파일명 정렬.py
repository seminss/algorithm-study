def solution(files):
    dic = dict()
    for file in files:
        head = ""
        tmp=file
        while tmp and not tmp[0].isdigit():
            head += tmp[0].lower()
            tmp=tmp[1:]
        if tmp and tmp[0] == '0':
            tmp=tmp[1:]
        number = ""
        while tmp and tmp[0].isdigit():
            number += tmp[0]
            tmp=tmp[1:]
        dic[file] = [head, int(number)]
    
    sorted_dic = sorted(dic.items(), key=lambda x: (x[1][0], x[1][1]))
    answer = [a[0] for a in sorted_dic]
    return answer

#원래는 deque를 사용해서 풀었는데, 런타임 에러가 났다,,(40점)
#질문하기를 보니까 (모든언어) 런타임 에러 난 사람들이 많았고, 파이썬 런타임 에러 난 사람들은 전부 deque를 사용한 것 같아서
#deque말고 그냥 list로 구현했다,, 왜 에러가 나는지는 모르겠다 ㅜ.ㅜ