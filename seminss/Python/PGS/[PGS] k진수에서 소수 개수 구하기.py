#2:50~3:20
def convert(n,k):
    result=''
    while n>0:
        result+=str(n%k)
        n=n//k
    return result[::-1]

def check(s):
    num=int(s)
    if num==1: return False
    for i in range(2,int(num**0.5+1)):
        if num%i==0:
            return False
    return True

def solution(n, k):
    answer = 0
    str=convert(n,k)
    arr=str.split('0')
    while arr:
        a=arr.pop()
        if a.isdigit() and check(a):
            answer+=1
    return answer

# 이 문제랑은 관련 없지만 k진법 -> 10진법으로 변환할 때는 
# int('숫자문자열',3) 과 같이 쓰면 3진법으로 표현된 문자열이 10진법으로 변환된다고 함
# 10진법 -> k진법으로 변환하는 건 구현해야 함