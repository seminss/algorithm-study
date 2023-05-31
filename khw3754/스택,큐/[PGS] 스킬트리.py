from collections import deque


def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        turn = [s for s in skill]
        turn = deque(turn)
        # 이 트리가 가능한지 검사
        for t in tree:
            # 순서가 있는 스킬인데
            if t in skill:
                # 순서가 맞으면
                if t == turn[0]:
                    turn.popleft()
                # 안 맞으면 다음 트리 검사
                else:
                    break
        # 정상적으로 종료됐으면 count
        else:
            answer += 1

    return answer