'''2023.6.22
14:40 ~ 15:59
'''
def add_menu(entry:list, menu:set):
    """
    기존 코스요리의 subset은 포함하지 않는다.
    """
    for m in menu:
        m = [c for c in m]
        if set(entry).issubset(menu):
            return
    menu.add(''.join(entry))
    return
    
    
def dfs(order:str, r:int, result:set, tmp:list, index:int):
    """
    nCr의 결과를 result에 저장한다.
    """
    if len(tmp) == r:
        menu = ''.join(tmp)
        result.add(menu)
    else:
        for i in range(index, len(order)):
            tmp.append(order[i])
            dfs(order, r, result, tmp, i+1)
            tmp.pop()

    
def combine(order):
    """
    nC2 ~ nCn까지의 모든 경우의 수 반환
    """
    result = set()
    for i in range(1, len(order) + 1):
        dfs(order, i, result, [], 0)
    return result
    

def solution(orders, course):
    """
    O(orders) <= 20 * 10
    combinations: dict에 모든 조합의 개수를 기록한다.
    """
    record = dict()
    orders.sort(key=lambda s:len(s))
    # O(N) <= 20*100
    for order in orders:
        order = ''.join(sorted([c for c in order]))
        # O(N) <= 1024
        temp_combinations = combine(order)
        for c in temp_combinations:
            if c in record:
                record[c] += 1
            else:
                record[c] = 1
    # 코스요리 구성
    frequency = dict() # x개의 메뉴로 구성된 코스요리의 주문 최대 횟수
    course_menu = dict() # x개의 메뉴로 구성된 코스요리
    for x in course:
        frequency[x] = 0
    for x in course:
        # 가장 많이 주문된 조합만 코스요리로 만든다.
        for k in record.keys():
            if record[k] >=2 and len(k) == x and frequency[x] < record[k]:
                frequency[x] = record[k]
                course_menu[x] = [k]
            elif record[k] >=2 and len(k) == x and frequency[x] == record[k]:
                course_menu[x].append(k)
    answer = []
    for m in course_menu.values():
        answer += m
    return sorted(answer)
