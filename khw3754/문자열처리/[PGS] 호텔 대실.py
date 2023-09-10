def makeTime(start):
    # 10분 빼줌
    h = int(start[0:2])
    m = int(start[3:]) - 10
    if m < 0:
        h -= 1
        m += 60

    if h < 10:
        result = '0' + str(h) + ':'
    else:
        result = str(h) + ':'
    if m < 10:
        result += '0' + str(m)
    else:
        result += str(m)

    return result


# 시작시간 순으로 정렬하고 하나씩 맞춰보면 될 듯 -> 가능한 것들 중에 가장 늦게 끝나는 것?
def solution(book_time):
    book_time = sorted(book_time, key=lambda x: x[0])
    rooms = [[book_time.pop(0)]]
    for start, end in book_time:
        makedStart = makeTime(start)
        targets = list(filter(lambda x: x[-1][1] <= makedStart, rooms))
        if len(targets) == 0:
            rooms.append([[start, end]])
        else:
            # 가장 늦게 끝나는 것으로 골라서 넣음
            last = sorted(targets, key=lambda x: x[-1][1])[-1]
            last.append([start, end])

    return len(rooms)