def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = list('0'+bin(number)[2:])
        idx=''.join(bin_number).rfind('0')
        bin_number[idx]='1'
        if number%2==1: #짝수인 경우에는 0->1 이 되었지만 홀수는 01->11이 되었으니 10ㅇ로 바꿔준다.
            bin_number[idx+1]='0'
        answer.append(int(''.join(bin_number),2)) #2진수를 다시 정수 변환
    return answer