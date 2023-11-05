import sys
import heapq


# 10:31~ 11:15

def back():
    global n, now, hq, q, decimal
    if len(now) > 0 and int(now) > 9876543210:
        return
    flag = True
    for num in decimal:
        if len(now) > 0 and num >= int(now[-1]):
            continue
        flag = False
        now = now + str(num)
        heapq.heappush(hq, int(now))
        back()
        now = now[:-1]
    if flag:
        q = heapq.nsmallest(n, hq)
        return


if __name__ == "__main__":
    n = int(sys.stdin.readline())
    hq, q = [], []
    now = ''
    decimal = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    back()
    if len(q) == n:
        print(q[-1])
    else:
        print(-1)

# 줄어드는 수는 주 중 가장 큰 값은 1000000 이 아니라 9876543210이다.. <<이게 키포인트..
# 100만은 경우의 수의 개수