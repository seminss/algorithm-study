def solution(s):
    answer = ''
    
    s = s.split(" ")
    print(s)
    
    for text in s :
        if text != "" and text[0].isalpha() :
            answer += text[0].upper() + text[1:].lower() + " "
        elif text != "" :
            answer += text[0] + text[1:].lower() + " "
        else :
            answer += " "
    
    answer = answer[:-1]
    return answer