def solution(dirs):
    answer=0
    dic={'U':(0,1),'D':(0,1),'R':(1,0),'L':(-1,0)}
    visited=set()
    present=(0,0)

    for d in dirs:
        x,y=present #이동 전 시작 점
        dx,dy=dic[d] # 튜플 값 하나씩 변수에 넣기
        nx,ny=x+dx,y+dy #이동 후 도착 점
        if -5<=nx<=5 and -5<=y<=5:
            path =(x,y,nx,ny) #이동 경로 (0,1) -> (0,2)
            reverse_path=(nx,ny,x,y) #돌아오는 경로도 막기 (0,2) -> (1,0)
            if path not in visited and reverse_path not in visited:
                visited.add(path)
                visited.add(reverse_path)
                answer+=1
            present=(nx,ny)
        return answer