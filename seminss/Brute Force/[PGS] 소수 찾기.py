#2:02~2:16
from itertools import permutations

def isdecimal(num):
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums=set()
    for i in range(1,len(numbers)+1):
        perm=set(permutations(numbers,i))
        for p in perm:
            n=''.join(p)
            n=n.lstrip('0')
            if n.isdigit() and n!='1':
                nums.add(int(n))

    for n in nums:
        if isdecimal(n):
            answer+=1
    return answer