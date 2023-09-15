# 단어 중복 x
# 한글자 x

def solution(n, words):
    answer = [0,0]
    
    for i in range(1, len(words)) :
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] :
            answer = [i%n+1, i//n +1] 
            break
    
    return answer