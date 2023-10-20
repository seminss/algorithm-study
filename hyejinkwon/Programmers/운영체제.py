'''
점수가 낮을 수록 우선순위 높음
중간에 우선순위 높은애가 호출되어도 중단 안되고 종료될때까지 실행
우선순위 == ? 먼저 호출 우선

[ 우선순위, 들어오는시간, 실행시간 ]
'''

import heapq
    

def solution(program):
    answer = [0]*11
    heap = [] # 대기열

    # 들어오는 시간 -> 우선순위 순서 정렬
    program.sort(key = lambda x : (x[1],x[0]))
    
    while len(program) > 0 or not len(heap) == 0:
        if len(heap) == 0 :
            time = program[0][1] # 현재시간 초기화
            
            # 현재시간 >= 다음꺼 들어오는 시간 -> heap 대기열에 넣기 
            # program.pop(0)
            while len(program) > 0 and time >= program[0][1] : 
                heapq.heappush(heap, program.pop(0))

        now = heapq.heappop(heap)
        answer[now[0]] += (time - now[1]) # 대기시간 계산
        time += now[2]
        while len(program) > 0 and time >= program[0][1] : 
                heapq.heappush(heap, program.pop(0))
                
    answer[0] = time
                
    return answer