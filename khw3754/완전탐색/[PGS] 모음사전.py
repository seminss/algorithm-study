# AUUUU     AEUUU
def next(w):
    next_alph = {'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U'}

    if len(w) != 5:
        return w + 'A'
    else:
        if w[4] != 'U':
            w = w[:4] + next_alph[w[4]]
            return w
        # 5번째 글자가 U인 경우
        else:
            # U를 모두 없애고
            while w[-1] == 'U':
                w = w[:-1]
            # 다음 글자로 교체
            w = w[:-1] + next_alph[w[-1]]

            return w


def solution(word):
    answer = 0
    check = ''

    while check != word:
        check = next(check)
        answer += 1

    return answer