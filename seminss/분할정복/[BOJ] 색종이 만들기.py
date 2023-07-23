import sys

n = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white = 0
blue = 0

def check(maps):
    global white, blue
    if all(0 not in line for line in maps):
        blue += 1
        return
    elif all(1 not in line for line in maps):
        white += 1
        return
    else:
        half = len(maps) // 2
        check([row[:half] for row in maps[:half]])
        check([row[half:] for row in maps[:half]])
        check([row[:half] for row in maps[half:]])
        check([row[half:] for row in maps[half:]])
check(maps)

print(white)
print(blue)