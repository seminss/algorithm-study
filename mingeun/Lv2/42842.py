''' 2023.6.1
15:00 ~ 15:18
'''
def prime_factors(n):
    factors = []
    # O(n) <= 2000
    for i in range(1, int(n**(1/2)) + 1):
        if n%i == 0:
            factors.append((i, n//i))
    return factors
    
def solution(brown, yellow):
    if yellow == 1:
        return [3, 3]
    Y = prime_factors(yellow)
    for y in Y:
        yellow_width, yellow_height = max(y), min(y)
        if (yellow_width + yellow_height)*2 + 4 == brown:
            return [yellow_width+2, yellow_height+2]
