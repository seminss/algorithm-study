import sys
import heapq

input = sys.stdin.readline

def isEmpty(num_dict) :
    for num, value in num_dict :
        if value > 0 :
            return False
    return True

T = int(input())
for _ in range(T) : 
    min_heap = []
    max_heap = []
    num_dict = {}

    k = int(input())
    
    for _ in range(k) :
        op, num = input().split()
        num = int(num)
    
        if op == "I" :
            if num in num_dict :
                num_dict[num] += 1
            else :
                num_dict[num] = 1
                heapq.heappush(min_heap, num)
                heapq.heappush(max_heap, -num)

        elif op == "D" :
            if not isEmpty(num_dict.items()) :
                if num == 1 : #최댓값
                    while -max_heap[0] not in num_dict or num_dict[-max_heap[0]] < 1 :
                        temp = -heapq.heappop(max_heap)
                        if temp in num_dict:
                            del(num_dict[temp])
                    num_dict[-max_heap[0]] -= 1
                else : # 최솟값
                    while min_heap[0] not in num_dict or num_dict[min_heap[0]] < 1 :
                        temp = heapq.heappop(min_heap)
                        if temp in num_dict :
                            del(num_dict[temp])
                    num_dict[min_heap[0]] -= 1


    if isEmpty(num_dict.items()) :
        print("EMPTY")
    else :
        while min_heap[0] not in num_dict or num_dict[min_heap[0]] < 1 :
            heapq.heappop(min_heap)
        while -max_heap[0] not in num_dict or num_dict[-max_heap[0]] < 1 :
            heapq.heappop(max_heap)
        
    print(-max_heap[0], min_heap[0])