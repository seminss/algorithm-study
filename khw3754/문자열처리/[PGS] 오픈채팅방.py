def solution(record):
    answer = []

    nickname = {}
    history = []

    for rec in record:
        rec = rec.split()
        state, id = rec[0], rec[1]
        if state == 'Enter' or state == 'Leave':
            history.append(id + ' ' + state)
            if state == 'Enter':
                nickname[id] = rec[2]
        else:
            nickname[id] = rec[2]

    # 메세지 생성
    for his in history:
        id, state = his.split()
        message = "님이 들어왔습니다." if state == 'Enter' else "님이 나갔습니다."
        answer.append(nickname[id] + message)

    return answer