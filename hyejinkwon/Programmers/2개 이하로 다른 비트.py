# x보다 크고 x와 비트가 1-2개 다른 수들 중 제일 작은 수

# x가 짝수 : ex) 4 -> 100 가장 뒤에 있는 0의 비트를 바꾸자 101
# x가 홀수 : ex) 7 -> 0111 가장 뒤에 있는 0의 비트를 바꾸고 인덱스 기억 (0번째) 1111
#                    0번째 다음 index의 비트를 바꾸자
#                    1011 

# bin 라이브러리 이용
# int(str,2) -> 2진수를 10진수로 변경

def solution(numbers):
    answer = []
    
    for n in numbers :
        bit_num = list('0' + bin(n)[2:])
        
        for i in range(len(bit_num)-1,-1,-1) :
            if bit_num[i] == '0' :
                break
        
        if n%2 == 0 : # 짝수
            bit_num[i] = '1'
            answer.append(int(''.join(bit_num),2))
        else : # 홀수 
            bit_num[i] = '1'
            if bit_num[i+1] == '1' :
                bit_num[i+1] = '0'
            else :
                bit_num[i+1] = '1'
            answer.append(int(''.join(bit_num),2))
    
    return answer