def solution(n, words):
    answer = [0, 0]

    last = words[0]
    dic = {last: 1}
    for i in range(1, len(words)):
        if last[-1] != words[i][0] or dic.get(words[i], 0) == 1:
            answer[0] = i % n + 1
            answer[1] = i // n + 1
            break
        last = words[i]
        dic[words[i]] = 1

    return answer