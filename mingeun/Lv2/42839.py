''' 2023.6.9
15:50 ~ 16:09
'''
def perm(numbers, arr, results, visited):
    if len(arr) != 0 and int(''.join(arr)) not in results:    
        results.add(int(''.join(arr)))
    for i in range(len(numbers)):
        if not visited[i]:
            arr.append(numbers[i])
            visited[i] = True
            perm(numbers, arr, results, visited)
            arr.pop()
            visited[i] = False

                
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**(1/2))+1):
        if (n%i) == 0:
            return False
    return True
            
            
def solution(numbers):
    answer = 0
    p = set()
    visited = [False] * len(numbers)
    perm(numbers, [], p, visited)
    for n in p:
        if is_prime(n):
            answer += 1
    return answer
