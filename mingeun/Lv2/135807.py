'''2023.7.27
17:30 ~ 18:30
'''
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
    
def solution(arrayA, arrayB):
    arrayA.sort()
    arrayB.sort()
    gcd_a, gcd_b = arrayA[0], arrayB[0]
    for i in range(1, len(arrayA)):
        gcd_a = gcd(gcd_a, arrayA[i])
        gcd_b = gcd(gcd_b, arrayB[i])
    answer = 0
    count_a, count_b = 0, 0
    for i in range(len(arrayA)):
        if arrayA[i] % gcd_b != 0:
            count_a += 1
        if arrayB[i] % gcd_a != 0:
            count_b += 1
    if count_a == count_b and count_a == len(arrayA):
        answer = max(gcd_a, gcd_b)
    elif count_a == len(arrayA):
        answer = gcd_b
    elif count_b == len(arrayB):
        answer = gcd_a
    else:
        answer = 0
    print(gcd_a, gcd_b)
    return answer
