'''2023.6.16
14:23 ~ 15:16
'''
def solution(sequence, k):
    l, r = 0, 0
    s = sequence[l]
    answer = [0, len(sequence)]
    while r < len(sequence):
        # print(f'l:{l} r:{r} s:{s} answer: {answer}')
        # 합이 k보다 작은 경우 r 증가
        if s < k:
            r += 1
            if r >= len(sequence):
                break
            s += sequence[r]
        # 합이 k보다 큰 경우 l 증가
        elif s > k:
            s -= sequence[l]
            l += 1
            if l > r:
                break
        # 부분수열의 합이 k가 됨
        elif s == k:
            if answer[1] - answer[0] > r - l:
                answer = [l, r]
            s -= sequence[l]
            l += 1
            r += 1
            if r < len(sequence):
                s += sequence[r]
            else:
                break
    return answer

'''
0 1 2 3 4 5 6
1 1 1 2 3 4 5
'''
