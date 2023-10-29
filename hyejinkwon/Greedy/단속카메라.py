def solution(routes):
    answer = 0
    
    # 고속도로 나간 시점 기준 정렬
    routes = sorted(routes, key = lambda x : x[1])
    print(routes)
    camera = -30001
    
    for come,out in routes :
        if camera < come : 
            camera = out    
            answer += 1
        
    return answer