'''2023.7.18
22:05 ~ 22:34
'''

def empty(s1:str, s2:str):
    """
    t1에 퇴실했을 때, t2가 입실 가능한지 확인
    """
    if len(s1) == 0: # 초기값
        return True
    t1 = 60*int(s1[:2]) + int(s1[3:])
    t2 = 60*int(s2[:2]) + int(s2[3:])
    return t1 + 10 <= t2
    
    
def solution(book_time):
    book_time.sort(key = lambda s: (int(s[0][:2]), int(s[0][3:])))
    room = [''] * len(book_time)
    for checkin, checkout in book_time:
        for i in range(len(room)):
            if empty(room[i], checkin):
                room[i] = checkout
                break
    answer = 0
    for r in room:
        if len(r) > 0:
            answer += 1
    return answer
