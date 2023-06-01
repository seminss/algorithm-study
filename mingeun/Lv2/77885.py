''' 2023.6.1
시간초과
'''
def solution(numbers):
    answer = []
    for n in numbers:
        # even number
        if n%2 == 0:
            answer.append(n + 1)
        # odd number
        else:
            '''
            5 = 101 -> 110
            9 = 1001 -> 1010
            '''
            zero_index = -1
            bin_str = str(bin(n))[2:]
            for i in range(len(bin_str)-1, -1, -1):
                if bin_str[i] == '0':
                    zero_index = len(bin_str) - 1 - i
                    break
            if zero_index == -1:
                zero_index = len(bin_str)
            answer.append(n + 2**(zero_index) - 2**(zero_index-1))
    return answer
