# 4:03 ~ 4:21
# 3*2^k -> 24=3*2^3
import sys


def size_up(tri):
    global n
    len_tri = len(tri)
    new_tri = tri * 2
    if len(tri) == n:
        for line in tri:
            print(line)
        return tri

    for i in range(len_tri):
        new_tri[i] = ' ' * len_tri + new_tri[i] + ' ' * len_tri

    for i in range(len_tri, len(new_tri)):
        new_tri[i] = new_tri[i] + ' ' + new_tri[i]
    size_up(new_tri)


if __name__ == "__main__":
    base_tri = ["  *  ", ' * * ', "*****"]
    n = int(sys.stdin.readline())
    size_up(base_tri)
