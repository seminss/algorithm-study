import sys


def quad(maps):
    n = len(maps)
    if n == 1:
        return maps[0]

    half = n // 2

    upper_left = quad([line[:half] for line in maps[:half]])
    upper_right = quad([line[half:] for line in maps[:half]])
    lower_left = quad([line[:half] for line in maps[half:]])
    lower_right = quad([line[half:] for line in maps[half:]])

    # print(upper_left , upper_right , lower_left , lower_right)
    if upper_left == upper_right == lower_left == lower_right:
        if '0' not in upper_right or '1' not in upper_right:  # 이 조건이 없으면 4, 0000/1111/0000/1111 에서 (0011) 이 반환됨
            return upper_left

    return f"({upper_left}{upper_right}{lower_left}{lower_right})"


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    maps = [input().strip() for _ in range(n)]
    answer = quad(maps)
    print(answer)

# 처음에는 재귀 탈출 조건을 걸어서 빠져나오게 했다. 이 경우 재정렬을 해야 하는 경우를 고려하지 못했다. >> (110(0101))(0010)(1111)(0001) 와 같은 결과
# 따라서 4방향 결과 값을 모두 저장해서 같은지 비교하고, 결과를 반환할 수 있도록 했다. 1111이면 1반환, 0010과 같이 다른게 섞여있으면 괄호로 묶어 반환
