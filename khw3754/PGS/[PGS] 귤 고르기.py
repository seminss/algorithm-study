def solution(k, tangerine):
    size = {}
    for i in tangerine:
        if size.get(i, -1) == -1:
            size[i] = 1
        else:
            size[i] += 1

    keys = sorted(size.keys(), key=lambda x: -size[x])

    count = 0
    for key in keys:
        if size[key] >= k:
            count += 1
            k = 0
            break
        else:
            k -= size[key]
            count += 1

    return count