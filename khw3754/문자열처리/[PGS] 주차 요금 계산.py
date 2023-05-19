'''
 출차된 내역이 없다면, 23:59에 출차된 것으로 간주
 단위 시간으로 나누어 떨어지지 않으면, 올림

 차량 번호가 작은 자동차부터
'''
from collections import defaultdict


def solution(fees, records):
    answer = []

    total = defaultdict(int)
    in_cars = {}
    for record in records:
        time, num, state = record.split()
        if state == 'IN':
            in_cars[num] = time

        else:
            out_h, out_m = map(int, time.split(':'))
            in_h, in_m = map(int, in_cars[num].split(':'))

            hour = out_h - in_h
            min = 0
            if out_m >= in_m:
                min = out_m - in_m
            else:
                min = 60 - in_m + out_m
                hour -= 1

            total[num] += hour * 60 + min

            del in_cars[num]

    # 출차가 안된 차량들
    for num, time in in_cars.items():
        out_h, out_m = 23, 59
        in_h, in_m = map(int, time.split(':'))

        hour = out_h - in_h
        min = out_m - in_m

        total[num] += hour * 60 + min

    # 시간 기록으로 요금 계산
    for num in sorted(total.keys()):
        if total[num] <= fees[0]:
            answer.append(fees[1])

        else:
            fee = fees[1] + (total[num] - fees[0]) // fees[2] * fees[3]
            if (total[num] - fees[0]) % fees[2] > 0:
                fee += fees[3]

            answer.append(fee)

    return answer