def solution(n):
    answer = 0
    i=1
    i_sum=0
    while i_sum<n:
        if (n-i_sum)%(i)==0:
            answer+=1
        i_sum+=i
        i+=1
    return answer