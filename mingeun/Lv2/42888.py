''' 2023.5.14
20:56 ~ 21:13
'''
def solution(record):
    '''
    중복 닉네임 허용(똑같은 닉네임이 여러 명 있을수 있다)
    record: ["Enter/Leave/Change {uid} {nickname}", ... ]
    users: {"uid": nickname}
    '''
    # 모든 유저의 최종 닉네임 결정. Leave의 경우 2개로 나누어진다.
    users = dict()
    for r in record:
        if len(r.split(' ')) == 3:
            act, uid, nickname = r.split(' ')
            users[uid] = nickname
    # 메세지 생성
    answer = []
    for r in record:
        str_subj, str_act = "", ""
        # Enter/Change
        if len(r.split(' ')) == 3:
            act, uid, _ = r.split(' ')
        # Leave
        else:
            act, uid = r.split(' ')
        if act == "Enter":
            str_act = "들어왔습니다."
            str_subj = users[uid] + "님이 "
            answer.append(str_subj + str_act)
        elif act == "Leave":
            str_act = "나갔습니다."
            str_subj = users[uid] + "님이 "
            answer.append(str_subj + str_act)
    return answer
