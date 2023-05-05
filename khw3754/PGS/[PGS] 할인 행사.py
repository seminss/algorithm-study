def solution(want, number, discount):
    answer = 0

    want_dict = {w: n for w, n in zip(want, number)}

    # 1일차부터 10일 단위로 확인
    for i in range(len(discount) - 9):
        wants = want_dict.copy()
        # 현재 일차부터 10일간 물품 확인
        for dis in discount[i:i + 10]:
            if wants.get(dis, -1) != -1:
                wants[dis] -= 1
        # 만약 모두 살 수 있다면 answer+1
        for val in wants.values():
            if val > 0:
                break
        else:
            answer += 1

    return answer