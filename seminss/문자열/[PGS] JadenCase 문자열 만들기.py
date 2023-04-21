def solution(s):
    s = s.lower()
    answer='*'+s+'*'
    s = s.split()
    
    for a in s:
        if a[0].isalpha():
            answer=answer.replace(' '+a+' ',' '+a.title()+' ')
        else:
            continue
    answer=answer.strip('*')
    return answer