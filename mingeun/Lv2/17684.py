''' 2023.5.7
16:59 ~ 17:21
'''
def solution(msg):
    answer = []
    alphabets = 'abcdefghijklmnopqrstuvwxyz'.upper()
    # 사전 초기화
    dictionary = dict()
    for i,c in enumerate(alphabets):
        dictionary[c] = i
    # 압축 시작
    i = 0
    while i < len(msg):
        hit = False
        # 사전에서 일치하는 가장 긴 문자열(msg[i:j]을 찾는다.)
        for j in range(len(msg), i, -1):
            # 사전에서 가장 긴 문자열 탐색
            if msg[i:j] in dictionary:
                answer.append(dictionary[msg[i:j]]+1)
                dictionary[msg[i:j+1]] = len(dictionary)
                i = j
    return answer
