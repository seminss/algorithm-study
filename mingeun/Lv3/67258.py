''' 2023.5.16
21:25 ~ 23:20
'''
def solution(gems):
    n = len(set(gems))
    left, right = 0, 0 # 0-index
    answer = [0, len(gems)-1]
    basket = dict()
    basket[gems[0]] = 1
    while left <= right < len(gems):
        # 아직 하나씩 담지 못함
        if len(basket) != n:
            right += 1
            if right == len(gems):
                break
            if gems[right] in basket:
                basket[gems[right]] += 1
            else:
                basket[gems[right]] = 1
        # 하나씩 다 담음
        else:
            # 답 갱신
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            elif right - left == answer[1] - answer[0] and left < answer[0]:
                answer = [left, right]
            basket[gems[left]] -= 1
            if basket[gems[left]] == 0:
                del basket[gems[left]]
            left += 1
    answer[0] += 1
    answer[1] += 1
    return answer
