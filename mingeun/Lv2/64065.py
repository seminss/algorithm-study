'''
튜플
https://school.programmers.co.kr/learn/courses/30/lessons/64065
'''

''' 2023.5.4
18:05 ~
'''

def solution(s):
    # s < 10^8
    '''
    {a} -> 튜플의 첫 번째 원소
    {b, a} -> a는 첫 번째, b는 두 번째
    '''
    numbers = dict()
    i = 0
    while i < len(s):
        # n-tuple -> numbers[n] = [숫자 리스트]
        if s[i].isdigit() and s[i-1] == '{':
            l = []
            n = 1
            numstr = ''
            while s[i]!='{' and s[i]!='}':
                if s[i].isdigit():
                    numstr += s[i]
                elif s[i] == ',':
                    l.append(int(numstr))
                    numstr = ''
                    n += 1
                i += 1
                if s[i] == '}':
                    l.append(int(numstr))
                    numbers[n] = l
        else: 
            i+=1
    tuple_size = len(numbers)
    used = set()
    answer = []
    for i in range(1, tuple_size+1):
        for num in numbers[i]:
            if num not in used:
                answer.append(num)
                used.add(num)
    return answer
