def cal_bfs(numbers, target, idx, sum_):
    count = 0
    if idx == len(numbers) - 1:
        if sum_ + numbers[idx] == target:
            count += 1
        if sum_ - numbers[idx] == target:
            count += 1
        return count

    count += cal_bfs(numbers, target, idx + 1, sum_ + numbers[idx])
    count += cal_bfs(numbers, target, idx + 1, sum_ - numbers[idx])

    return count


def solution(numbers, target):
    answer = cal_bfs(numbers, target, 0, 0)
    return answer