import sys

input = sys.stdin.readline
count0 = [1,0,1]
count1 = [0,1,1]

# f(n) = f(n-1) + f(n-2)

def fibonacci(n) :
    if n >= len(count0) :
        for i in range(len(count0),n+1) :
            count0.append(count0[i-1] + count0[i-2])
            count1.append(count1[i-1] + count1[i-2])

    print(count0[n], count1[n])

T = int(input())
for _ in range(T) :
    fibonacci(int(input()))
