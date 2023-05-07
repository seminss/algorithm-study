from collections import deque

def solution(numbers, target):
    operators = [-1, 1]
    answer = 0
 	# bfs - 각 노드는 숫자들의 합, 간선은 - 또는 +, depth는 부호가 붙을 숫자의 인덱스
    depth = 0
    queue = deque([(depth, numbers[0]), (depth, -numbers[0])])
    while queue:
        d, s = queue.popleft()
        # target이 완성된 경우
        if d == len(numbers) - 1:
            if s == target:
                answer += 1
        # 아직 연산 중
        else:
            for i in range(2):
                queue.append((d+1, operators[i]*numbers[d+1] + s))
    return answer
