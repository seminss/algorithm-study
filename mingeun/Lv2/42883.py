def dfs(index:int, number:str, arr:list, combinations:list, k:int):
    """
    number의 숫자 중 k개를 제외한 숫자를 combinations에 저장한다.
    """
    if len(arr) == len(number)-k:
        combinations.append(int(''.join(arr)))
        # print(''.join(arr))
        return
    else:
        for i in range(index, len(number)):
            arr.append(number[i])
            dfs(i+1, number, arr, combinations, k)
            arr.pop()
        return
    
    
def solution(number, k):
    answer = ''
    combinations = []
    dfs(0, number, [], combinations, k)
    return str(max(combinations))

print(solution("898919", 3))
