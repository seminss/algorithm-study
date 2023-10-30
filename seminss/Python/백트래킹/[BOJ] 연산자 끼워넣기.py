import sys
from collections import deque


def back(result):
    origin_res = int(result)
    global min_res, max_res,cal_dic,nums
    if len(nums) == 0:
        if result < min_res:
            min_res = result
        if result > max_res:
            max_res = result
        return
    for k, v in cal_dic.items():
        if v == 0:
            continue
        t = nums.popleft()
        cal_dic[k] -= 1
        # print(f"{res}{k}{t}=", end='')
        if result < 0 and k == '//':
            result = -(-result // t)
        else:
            result = eval(f"{result}{k}{t}")

        back(result)
        result = origin_res
        nums.insert(0, t)
        cal_dic[k] += 1


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    nums = deque(list(map(int, sys.stdin.readline().strip().split())))

    cals_cnt = list(map(int, sys.stdin.readline().split()))
    cal_dic = {'+': cals_cnt[0], '-': cals_cnt[1], '*': cals_cnt[2], '//': cals_cnt[3]}
    min_res, max_res = 1e10, -1e10
    res = nums.popleft()
    back(res)
    print(max_res)
    print(min_res)


# 연산자 우선 순위를 무시, 앞에서 부터 진행
# 음수를 양수로 나누는 경우를 고려 해야 한다!!!!! 문제를 꼼꼼히 좀 읽자...
