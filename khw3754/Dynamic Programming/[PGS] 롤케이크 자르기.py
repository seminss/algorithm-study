from collections import defaultdict


def solution(topping):
    answer = 0

    leftTopp = defaultdict(int)
    rightTopp = defaultdict(int)
    for i in topping:
        rightTopp[i] += 1

    for topp in topping:
        leftTopp[topp] += 1

        rightTopp[topp] -= 1
        if rightTopp[topp] == 0:
            del rightTopp[topp]

        if len(leftTopp) == len(rightTopp):
            answer += 1

    return answer