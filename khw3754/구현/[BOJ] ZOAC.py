S = input()
sortedS = sorted(S)

def orders(s):
    if len(s) == 1:
        return [0]

    result = []
    sortedS = sorted(s)
    firstIdx = s.index(sortedS[0])
    result.append(firstIdx)

    # 오른쪽이 있으면
    if firstIdx != len(s) - 1:
        right_result = orders(s[firstIdx + 1:])
        right_result = map(lambda x: x + firstIdx + 1, right_result)
        result.extend(right_result)

    # 왼쪽이 있으면
    if firstIdx != 0:
        left_result = orders(s[:firstIdx])
        result.extend(left_result)

    return result

orderList = orders(S)
for length in range(1, len(orderList) + 1):
    string = ""
    for i in sorted(orderList[:length]):
        string += S[i]
    print(string)