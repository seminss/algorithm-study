def solution(n, lost, reserve):

    # 진짜 여분이 있는 학생
    _reserve = [r for r in reserve if r not in lost ]
    _reserve.sort()
    # 진짜 체육복 없는 학생
    _lost = [l for l in lost if l not in reserve]
    _lost.sort()
    for r in _reserve :        
        if r-1 in _lost :
            _lost.remove(r-1)
        elif r+1 in _lost :
            _lost.remove(r+1)
    
    return n - len(_lost)


