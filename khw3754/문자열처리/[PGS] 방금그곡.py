# '#'을 없애주는 함수
def change_sheet(s):
    result = s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return result


def solution(m, musicinfos):
    answer = ''
    m = change_sheet(m)

    # (제목, 재생된 악보) 가 들어가는 리스트
    musics = []
    for music in musicinfos:
        sta, end, title, sheet = music.split(',')
        sta_h, sta_m = map(int, sta.split(':'))
        end_h, end_m = map(int, end.split(':'))

        count = (end_h - sta_h) * 60 + end_m - sta_m

        sheet = change_sheet(sheet)

        tmp = sheet
        while len(tmp) < count:
            tmp += sheet
        tmp = tmp[:count]

        musics.append((title, tmp))

    targets = []
    for t, s in musics:
        if m in s:
            targets.append((t, s))

    print(musics)

    if len(targets) == 0:
        return "(None)"
    elif len(targets) == 1:
        return targets[0][0]
    # 조건이 일치하는 음악이 여러 개일 때
    else:
        max_len = 0
        result = ''
        for t, s in targets:
            if max_len < len(s):
                max_len = len(s)
                result = t
        return result