import heapq

'''
def solution(operations):
    answer = []
    heap = []
    
    for op in operations :
        oper, val = op.split()
        val = int(val)
        
        if oper == "I" :
            heapq.heappush(heap, val)
            
        elif oper == "D" and val == 1 and heap!=[] :
            heap.remove(heap[-1])
            
        elif oper == "D" and val == -1 and heap!=[]:
            heapq.heappop(heap)
        
    if heap!= [] :
        answer = [max(heap),min(heap)]
    else :
        answer = [0,0]
    
    return answer
'''

import heapq

def solution(operations):
    answer = []
    maxheap = []
    minheap = []
    
    for op in operations :
        oper, val = op.split()
        val = int(val)
        
        if oper == "I" :
            heapq.heappush(maxheap, -1*val)
            heapq.heappush(minheap, val)
            
        elif oper == "D" and val == 1 and maxheap != [] :
            minheap.remove(-1*heapq.heappop(maxheap))
            
        elif oper == "D" and val == -1 and minheap != [] :
            maxheap.remove(-1*heapq.heappop(minheap))
            
    if minheap == [] : answer = [0,0]
    else : answer = [-1*heapq.heappop(maxheap), heapq.heappop(minheap)]
    
    return answer