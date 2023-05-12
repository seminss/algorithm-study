def change(n, length) :
    result = '0'
    start = 1
    alpha = ['A','B','C','D','E','F']
    
    while len(result) < length:
        test = ''
        i = start
        while i != 0 :
            if i%n >= 10 :
                test += str(alpha[(i%n)%10])
            else :
                test += str(i%n)
            i //= n
        
        result += test[::-1]
        start += 1

    return result

def solution(n, t, m, p):
    answer = ''
    round = change(n, m*t)

    for i in range(p-1, len(round), m):
        if len(answer) == t :
            break
        answer += round[i]
            
    return answer