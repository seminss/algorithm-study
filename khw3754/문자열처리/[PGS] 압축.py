def solution(msg):
    answer = []

    dic = {chr(al): al - ord('A') + 1 for al in range(ord('A'), ord('Z') + 1)}

    pos = 0
    while pos < len(msg):
        # 먼저 사전에 있는 단어를 찾음
        poslen = 1
        word = msg[pos: pos + poslen]
        while dic.get(word, -1) != -1 and pos + poslen <= len(msg):
            poslen += 1
            word = msg[pos: pos + poslen]
        else:
            # 사전에 없는 단어 등록 (끝 부분일 경우 등록 방지)
            if pos + poslen < len(msg):
                dic[word] = len(dic) + 1
            # 사전에 있는 단어로 되돌림
            poslen -= 1
            word = msg[pos: pos + poslen]

        # 출력
        answer.append(dic.get(word, -1))
        pos += poslen

    return answer