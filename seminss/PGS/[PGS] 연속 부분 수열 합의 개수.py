#11:50 ~ 12:07
# 1 4 7 9 1 1 4 7 9

def solution(elements):
    case=set()
    caseSize=len(elements)
    elements=elements*2
    for i in range(caseSize):
        for j in range(caseSize):
            case.add(sum(elements[j:j+i+1]))
    return len(case)

# 처음에는 case를 list 자료형으로 선언하고 for문 내에서 sum 값이 list 안에 있는지 확인하는 로직을 넣어 중복 저장을 방지했다. 
# 그랬더니 시간초과가 남
# set() 으로 선언하면 자동으로 중복값이 들어가지 않는다!!!!