import sys
from fractions import Fraction
n,m=map(int,sys.stdin.readline().split())
fact=[0]*(n+1)
fact[1]=1
for i in range(2,n+1):
    fact[i]=fact[i-1]*i
print(Fraction(fact[n],(fact[n-m]*fact[m])))

#분수로 만들고 싶을 때는 Fraction(=분수)을 사용해야 한다.
#단순 나눗셈 연산을 쓰면 오차가 발생해서 틀린다,,