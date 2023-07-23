# 음악 길이 > 재생된 시간 : 음악 끊김 없이 처음부터 반복해서 재생됨
# 음악길이 < 재생된 시간 : 처음부터 재생 시간만큼만 재생됨

# C# D# F# G# A# 문자 주의 : 소문자로 치환
# 순서 중요 1. 문자치환 2. melody의 길이 파악

def solution(m, musicinfos):
    
    answer = ''
    max_playtime = 0
    music_list = []
    index = -1
    
    for music in musicinfos :
        index += 1
        start,end,title, melody_or = music.split(",")
        start_h, start_m = start.split(":")
        end_h, end_m = end.split(":")
        playtime = (int(end_h)*60 + int(end_m)) - (int(start_h)*60 + int(start_m))
    
        melody_or = melody_or.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
        m = m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    
        melody = melody_or*(playtime//len(melody_or)) + melody_or[:playtime%len(melody_or)]
        
        if m in melody:
            music_list.append([playtime,index, title])
        
    if music_list == []:
        return "(None)"   
    else :
        music_list = sorted(music_list, key = lambda x : (-x[0], x[1]))
        answer = music_list[0][2]
        
    return answer