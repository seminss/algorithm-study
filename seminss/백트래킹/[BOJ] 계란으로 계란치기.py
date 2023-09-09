import sys


def count_broken_eggs(eggs):
    count = 0
    for egg in eggs:
        if egg[0] <= 0:
            count += 1
    return count


def back(now, eggs):
    global answer

    broken_eggs = count_broken_eggs(eggs)
    if broken_eggs > answer:
        answer = broken_eggs

    # 계란을 모두 둘었거나 모든 계란이 깨져있는 경우
    if now == len(eggs) or broken_eggs == len(eggs):
        return

    # 현재 계란이 깨져 있으므로 다른 계란을 깰 수 없다.
    if eggs[now][0] <= 0:
        back(now + 1, eggs)
        return

    all_broken = True
    for i in range(len(eggs)):
        if i == now or eggs[i][0] <= 0:
            continue
        all_broken = False
        eggs[i][0] -= eggs[now][1]
        eggs[now][0] -= eggs[i][1]
        back(now + 1, eggs)
        eggs[i][0] += eggs[now][1]
        eggs[now][0] += eggs[i][1]

    # 현재 계란은 깨지지 않았지만, 더이상 깰 수 있는 다른 계란이 없다.
    if all_broken:
        return

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    answer = float('-inf')
    eggs = []
    for _ in range(n):
        eggs.append(list(map(int, sys.stdin.readline().strip().split())))
    back(0, eggs)
    print(answer)

# eggs[i][0] 내구도, eggs[i][1] 무게
# 현재 든 계란이 깨질 때까지 치는게 아니라, 한번 쳤으면 바로 오른쪽 거 들어서 치는 것

# 깨진 계란의 개수를 len(list(filter(lambda x: x[0] <= 0, eggs))) 로 셌을 때 계속 시간 초과가 났었고,
# 이 부분을 for문을 통해 직접 세주니 시간 초과가 안났다.
# len,list,filter를 사용하면 filter 객체가 메모리에 별도로 생성되고, list 객체도 새로 생성된다.
# 이 과정에서 메모리 사용량, 시간 복잡도가 높아졌을 것이다.
