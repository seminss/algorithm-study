from collections import defaultdict
def solution(s):
    # 문자열 가공
    s = s.replace('}','').split('{')[2:]
    # print(s)
    for i in range(len(s)):
        if s[i][-1] == ',':
            s[i] = s[i][:-1]
    # print(s)
    s = list(map(lambda x: list(map(int, x.split(','))), s))
    # print(s)
    s = sorted(s, key=lambda x: (len(x), x[-1]))
    # print(s)

    # 결과, result의 수의 개수 count하는 딕셔너리
    result = []
    count = defaultdict(int)
    # 각 stage 별로 처리
    for stage in s:
        tmp_count = count.copy()
        for i in stage:
            tmp = tmp_count.get(i, -1)
            # 만약 count에 없는 거면 추가
            if tmp == -1 or tmp == 0:
                result.append(i)
                count[i] += 1
                break
            else:
                tmp_count[i] -= 1


    return result