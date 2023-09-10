'''2023.7.14
21:05 ~ 
'''
def prioritize(ops, results, tmp):
    """
    연산자 우선순위 결정
    """
    if len(tmp) == len(ops):
        results.append(list(tmp))
        return
    else:
        for i in range(len(ops)):
            if ops[i] not in tmp:
                tmp.append(ops[i])
                prioritize(ops, results, tmp)
                tmp.pop()
    return


def operators(expression):
    result = []
    for c in expression:
        if not c.isdigit() and c not in result:
            result.append(c)
    return result


def mid2post(expression:str, priority:list) -> str:
    num = ''
    result = ''
    ops = []
    for i, c in enumerate(expression):
        # 숫자는 그냥 출력
        if c.isdigit():
            num += c
            if i == len(expression) - 1:
                result += ' ' + num
        # 연산자
        else:
            if len(result) == 0:
                result += num
            else:
                result += ' ' + num
            num = ''
            # 스택이 비었거나 우선순위가 높은 경우 스택에 삽입
            if len(ops) == 0 or priority.index(c) > priority.index(ops[-1]):
                ops.append(c)
            # 우선순위가 낮은 경우 스택의 연산자의 우선순위가 높거나 같은 동안 pop
            else:
                while len(ops) > 0 and priority.index(ops[-1]) >= priority.index(c):
                    result += ' ' + ops.pop()
                ops.append(c)
    while ops:
        result += ' ' + ops.pop()
    return result
    
    
def calculate(postfix):
    expr = postfix.split(' ')
    r, l = None, None
    stack = []
    for x in expr:
        if x.isdigit():
            stack.append(int(x))
        else:
            r, l = int(stack.pop()), int(stack.pop())
            if x == '*': stack.append(l*r)
            elif x == '+': stack.append(l+r)
            elif x == '-': stack.append(l-r)
    return abs(stack[-1])
        
                
def solution(expression):
    priorities = []
    prioritize(operators(expression), priorities, [])
    # 중위 -> 후위 표현식 전환
    answer = 0
    for p in priorities:
        postfix = mid2post(expression, p)
        answer = max(answer, calculate(postfix))
    return answer
