'''2023.08.04
-1
'''
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

    
"""
(a, b)를 최대공약수로 나눈 값을 반환
"""
def tan(a, b):
    d = gcd(a, b)
    return (a//d, b//d)
    
    
def solution(w,h):
    """
    직선이 양 꼭짓점을 지나는 가로 세로 길이가 서로소인 사각형을 지나는 경우 자르게 되는 사각형의 개수는 _w+_h-1
    """
    # 반복되는 작은 사각형에서 멀쩡하지 않은 사각형의 개수를 구한다.
    _w, _h = tan(w, h)
    # 작은 사각형 하나에서 멀쩡하지 않은 사각형의 개수를 구한다.
    incomplete_squares = (_w + _h - 1) * (w//_w)
    return w*h - incomplete_squares
