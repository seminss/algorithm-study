#9:48~9:57

def check(skill, tree):
    tmp=[i for i in skill]
    for t in tree:
        if t in tmp:
            if t==tmp[0]:
                tmp.pop(0)
            else:
                return False
    return True

def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        if check(skill,tree):
            print(tree)
            answer+=1
    return answer