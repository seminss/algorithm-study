'''
6 = 0110 -> 0111
7 = 0111 -> 1011
8 = 1000 -> 1001
9 = 1001 -> 1010
10 = 1010 -> 1011
11 = 1011 -> 1101
11011 -> 11101

## 뒤에서 첫 번째 0비트를 1로 바꾼 후 바로 그 뒤 비트를 0으로 두고 나머지는 원상태 유지
'''

def solution(numbers):
    answer = []

    for num in numbers:
        target = ('0' + bin(num)[2:])[::-1]

        idx = target.index('0')
        if idx == 0:
            result = '1' + target[1:]
        else:
            result = target[:idx - 1] + '01' + target[idx + 1:]

        answer.append(int(result[::-1], 2))

    return answer