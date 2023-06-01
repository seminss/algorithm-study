'''
먼저 파일 각각 head, number를 추출하여
[[파일명, head, number], ...] 형태로 저장한 후
1.head, 2.number 순으로 정렬
'''

def solution(files):
    nums = '0123456789'
    files_sort = []
    for file in files:
        num_start_idx = -1
        num_end_idx = len(file)
        finded = False
        for i, f in enumerate(file):
            if not finded and f in nums:
                num_start_idx = i
                finded = True
            elif finded and f not in nums:
                num_end_idx = i
                break

        files_sort.append([file, file[:num_start_idx].lower(), int(file[num_start_idx:num_end_idx])])

    files_sort = sorted(files_sort, key=lambda x: (x[1], x[2]))
    print(files_sort)
    answer = [i[0] for i in files_sort]

    return answer