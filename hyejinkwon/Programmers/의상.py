# 최소 1개의 의상을 입음

# a b1b2 c
# 1*2*1 = 2
# 2개면 1*2 + 2*1 + 1*1 = 2+2+1 = 5
# 2*3*2 = 12 -1

def solution(clothes):
    answer = 0
    result = 1 
    
    clothes_dict = {}
    clothes_kind_len = []
    
    for name,kind in clothes :
        if kind in clothes_dict :
            clothes_dict[kind].append(name)
        else :
            clothes_dict[kind] = [name]
    
    answer = len(clothes)
    
    combi_kinds = len(list(clothes_dict.keys()))  
    
    for key,value in clothes_dict.items() :
        clothes_kind_len.append(len(value))

    if combi_kinds >= 2 :
        for c in clothes_kind_len : 
            result *= c+1
    else :
        return answer 
    answer = result-1
    return answer