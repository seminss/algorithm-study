def solution(numbers, target):
    answer = 0
    can = [0]
    for num in numbers:
        new_can = []
        for c in can:
            new_can.append(c + num)
            new_can.append(c - num)
        can = new_can
    answer = can.count(target)
    return answer