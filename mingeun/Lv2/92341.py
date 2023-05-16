''' 2023.5.14
16:21 ~ 17:15
'''
import math

def minutes(timestamp):
    '''
    HH:MM -> int(M)
    '''
    hours = int(timestamp[:2])
    minutes = int(timestamp[-2:])
    return hours * 60 + minutes
    
    
def calculate(fees, in_out):
    """
    in_out: [(s1, e1), (s2, e2), ...]
    s: 입차 시각(분)
    e: 나간 시각(분)
    """
    min_time, min_rate, unit_time, unit_rate = fees
    result = 0
    # 누적 이용 시간
    total = 0
    for i in range(len(in_out)):
        s, e = in_out[i]
        total += e - s
    # 기본시간 이하 -> 기본 요금 부과
    if total <= min_time:
        result += min_rate
    # (기본 요금) + ceil[(초과 시간)/단위시간] * 기본 요금
    else:
        result += int(min_rate + math.ceil((total - min_time)/unit_time)*unit_rate)
    return result
        
    
def solution(fees, records):
    '''
    fees: 기본시간 기본요금 단위시간 단위요금
    records: 시각 차량번호 내역
    '''
    IN, OUT = 2, 3
    numbers = [] # 차량 번호 오름차순 정렬
    in_out = dict() # {차량 번호: [[입차시각, 출차 시각], [.,.]]}
    for r in records:
        timestamp, number, act = r.split(' ')
        if len(act) == IN:
            # 나갔다가 다시 들어온 경우
            if number in in_out:
                in_out[number].append([minutes(timestamp)])
            # 처음 들어온 경우
            else:
                in_out[number] = [[minutes(timestamp)]]
                numbers.append(number)
        elif len(act) == OUT:
            in_out[number][-1].append(minutes(timestamp))
    numbers.sort()
    # 출차 기록이 없는 차량의 출차 시각을 23:59로 설정
    for number in in_out:
        if len(in_out[number][-1]) == 1:
            in_out[number][-1].append(minutes("23:59"))
    # 계산
    print(numbers)
    answer = []
    for number in numbers:
        answer.append(calculate(fees, in_out[number]))
    return answer
