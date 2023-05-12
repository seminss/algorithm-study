def solution(msg):
    answer = []
    dict_msg = {}
    idx = 27
    for i in range(1,27) :
        dict_msg[chr(ord('A') + (i-1))] = i
    
    start, end = 0, 1
    while end < len(msg)+1 :
        mm = msg[start:end]
        if mm in dict_msg :
            end += 1
        else :
            answer.append(dict_msg[mm[:-1]])
            dict_msg[mm] = idx
            idx += 1
            start = end - 1
    answer.append(dict_msg[mm])
                
    return answer