def toBin(n):
    b=""
    while n!=0:
        b+=str(n%2)
        n=n//2
    return "".join(reversed(b))

def solution(n):
    answer = n+1
    b_num=toBin(n)
    while True:
        if toBin(answer).count('1') == toBin(n).count('1'):
            return answer
        answer += 1
    return answer