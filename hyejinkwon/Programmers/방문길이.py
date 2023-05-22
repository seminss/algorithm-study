def solution(dirs):
    answer = 0
    road = set([])
    
    x = 0
    y = 0
    
    for d in dirs :
        before_x , before_y = x,y
        if d == "U" and y < 5 : 
            x, y = x , y+1
            road.add((before_x , before_y,x,y))
        elif d == "L" and x >-5:
            x, y = x-1 , y
            road.add((before_x , before_y,x,y))
        elif d == "R" and x < 5:
            x, y = x+1 , y
            road.add((x,y,before_x , before_y))
        elif d == "D" and y > -5 :
            x, y = x , y-1
            road.add((x,y,before_x , before_y))
            
    answer = len(road)
    
    return answer