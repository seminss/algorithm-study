def solution(n, a, b):
    answer = 1

    while True:
        # a와b가 1차이고, 더 작은 게 홀수라면 -> 대결 상대
        if abs(a - b) == 1 and min(a, b) % 2 == 1:
            break

        # 대결 상대가 아니면 다음 라운드의 번호로 바꿔줌
        a = a // 2 if a % 2 == 0 else a // 2 + 1
        b = b // 2 if b % 2 == 0 else b // 2 + 1
        answer += 1

    return answer