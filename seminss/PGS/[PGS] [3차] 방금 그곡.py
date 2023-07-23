#10:43~11:30
#시작 시각, 끝난 시각, 음악 제목, 악보 정보
from collections import defaultdict
def solution(m, musicinfos):
    answer = ''
    dict={}
    m=m.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
    for musicinfo in musicinfos:
        start,end,title,info=map(str,musicinfo.split(","))
        info_list=list(c for c in info)
        s_h,s_m=map(int,start.split(":"))
        e_h,e_m=map(int,end.split(":"))
        time=(e_h-s_h)*60+(e_m-s_m)
        info=info.replace("C#","c").replace("D#","d").replace("F#","f").replace("G#","g").replace("A#","a")
        dict[title]="".join(list(info[i%len(info)] for i in range(time)))
    for k,v in dict.items():
        if m in v:
            if answer=="":
                answer=k
            elif len(dict[answer])<len(v):
                answer=k
    if len(answer)==0:
        return "(None)"
    else:
        return answer

# (풀이참고) 올림음은 replace 해주어야 하나의 계이름으로 판단되어진다..! 안하면 C#은 C와 #으로 쪼개짐