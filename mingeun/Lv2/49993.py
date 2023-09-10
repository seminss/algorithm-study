''' 2023.5.20
16:57 ~ 
'''

from collections import deque
def valid(skill, tree):
    skill = deque(skill)
    for c in tree:
        if c not in skill:
            continue
        elif skill[0] == c:
            skill.popleft()
        elif skill[0] != c:
            return False
    return True
            

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        if valid(skill, tree):
            answer += 1
    return answer
