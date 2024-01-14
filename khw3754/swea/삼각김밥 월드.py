T = int(input())

num = 1
length = 1
height = 0

triMap = {}

while num < 10001:
    for width in range(length):
        triMap[num] = [height, width]

        num += 1

    length += 1
    height += 1

for case in range(1, T+1):
    sta, end = map(int, input().split())

    if sta < end:
        sta, end = end, sta

    result = 0
    staH, staW = triMap[sta]
    endH, endW = triMap[end]

    while staH != endH or staW != endW:
        if staH == endH:
            result += abs(staW - endW)
            staW = endW
        elif staW == endW:
            result += abs(staH - endH)
            staH = endH
        elif staH != endH and staW != endW:
            # 같은 행이든 같은 열로 만들면 됨
            countH = abs(staH - endH)
            countW = abs(staW - endW)

            if countH <= countW:
                if endW < staW:
                    staW -= countH
                    staH -= countH
                else:
                    staH -= countH
                result += countH
            else:
                if endW < staW:
                    staW -= countW
                    staH -= countW
                else:
                    staW += countW
                result += countW

    print(f'#{case} {result}')