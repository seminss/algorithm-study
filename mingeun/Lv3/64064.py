''' 2023.5.16
16:35 ~ 21:07
'''
def compatible(user_id:str, banned_id:str) -> bool:
    if len(user_id) != len(banned_id):
        return False
    for i in range(len(user_id)):
        if banned_id[i] == '*':
            continue
        elif banned_id[i] != user_id[i]:
            return False
    return True
        
    
def nCr(user_id, r, arr, index, combinations):
    if len(arr) == r:
        combinations.append(list(arr)) # deep copy
    else:
        for i in range(index, len(user_id)):
            arr.append(user_id[i])
            nCr(user_id, r, arr, i+1, combinations)
            arr.pop()
            
            
def permutation(banned_id, arr, permutations):
    if len(arr) == len(banned_id):
        permutations.append([banned_id[i] for i in arr])
    else:
        for i in range(len(banned_id)):
            if i not in arr:
                arr.append(i)
                permutation(banned_id, arr, permutations)
                arr.pop()

                
def count_star(s):
    result = 0
    for c in s:
        if c == '*':
            result += 1
    return result


def does_map(user_id, banned_id):
    # banned_id의 모든 순열에 대해 대응되는 경우가 있는지 조사한다.
    per = []
    permutation(banned_id, [], per)
    for tmp in per:
        hit = []
        while tmp:
            target = tmp.pop()
            for uid in user_id:
                if compatible(uid,target) and uid not in hit:
                    hit.append(uid)
                    break
        # 하나라도 맞으면 바로 True 반환
        if len(hit) == len(banned_id):
            return True
    return False
            
    
def solution(user_id, banned_id):
    answer = 0
    combinations = []
    # 가능한 모든 조합을 구한다.
    nCr(user_id, len(banned_id), [], 0, combinations)
    # 각 조합 중 banned_id에 맞는 것의 개수를 센다.
    for comb in combinations:
        if does_map(comb, banned_id):
            # print(f'hit: {comb} {banned_id}')
            answer += 1
    return answer
