# 11:06 ~ 11:42

import sys


def size_up(sq):
    global n
    len_sq = len(sq)
    new_sq = sq * 3
    if len(sq) == n:
        for line in sq:
            print(line)
        return sq

    for i in range(len_sq):
        new_sq[i] = new_sq[i] * 3

    for i in range(len_sq, len_sq * 2):
        new_sq[i] = new_sq[i] + ' ' * len_sq + new_sq[i]

    for i in range(len_sq * 2, len_sq * 3):
        new_sq[i] = new_sq[i] * 3

    size_up(new_sq)


if __name__ == "__main__":
    base_sq = ["***", '* *', "***"]
    n = int(sys.stdin.readline())
    size_up(base_sq)

# 작은 sq가 더 큰 sq의 한 조각이 된다.
# for 문에서 라인을 참조하는 것은 복사하는 것, 그걸 그대로 수정해도 실제 리스트에 반영되지 않는다.
# 리스트를 슬라이싱 해서 참조해도 복사한 것과 같이 동작한다.
