def split_block(arr):
    result = []
    result.append(list(map(lambda x: x[:len(x) // 2], arr[:len(arr) // 2])))
    result.append(list(map(lambda x: x[len(x) // 2:], arr[:len(arr) // 2])))
    result.append(list(map(lambda x: x[:len(x) // 2], arr[len(arr) // 2:])))
    result.append(list(map(lambda x: x[len(x) // 2:], arr[len(arr) // 2:])))

    return result


def count_num(result):
    count0 = 0
    count1 = 0

    if result == 0:
        return 1, 0
    elif result == 1:
        return 0, 1

    for i in range(len(result)):
        if result[i] == 0:
            count0 += 1
        elif result[i] == 1:
            count1 += 1
        elif len(result[i]) > 1:
            a, b = count_num(result[i])
            count0 += a
            count1 += b

    return count0, count1


def zip_block(block):
    result = []

    if len(block) == 1:
        return block[0][0]

    can_zip = True
    data = block[0][0]
    for i in range(len(block)):
        for j in range(len(block[0])):
            if block[i][j] != data:
                can_zip = False
                break

    if can_zip:
        return data
    else:
        splited_blocks = split_block(block)

        for splited_block in splited_blocks:
            result.append(zip_block(splited_block))

        return result


def solution(arr):
    answer = count_num(zip_block(arr))
    return answer