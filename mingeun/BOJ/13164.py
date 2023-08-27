'''2023.8.12
-1
'''
import sys


def read_integers():
    return list(map(int, sys.stdin.readline().split(' ')))


def solution():
    # k <= n <= 300K
    n, k = read_integers()
    heights = read_integers()
    # n-1개의 차이(gap)이 생긴다.
    gaps = [heights[i+1] - heights[i] for i in range(n-1)]
    """
    k개의 그룹 -> (k-1)개의 gap을 선택하는 것이다.
    이 때 gap을 큰 순서대로 (k-1)개 선택하면
    각 그룹의 최소와 최대의 차이가 최소가 된다.
    그리고 그룹들의 비용의 합은 (k-1)개의 gap을 제외한 나머지의 gap들의 합이다.
    """
    gaps.sort(reverse=True)
    print(sum(gaps[k-1:]))


solution()
