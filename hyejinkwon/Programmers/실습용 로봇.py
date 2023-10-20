def solution(command):
    answer = [0, 0]
    direction = [ [0,1], [1,0], [0,-1], [-1,0] ]
    x = y = d = 0
    
    for c in command :
        if c == "R" : d = (d+1)%4
        elif c == "L" : d = (d+3)%4
        elif c == "G" :
            x += direction[d][0]
            y += direction[d][1]
        elif c == "B" :
            x -= direction[d][0]
            y -= direction[d][1]
    
    return [x,y]