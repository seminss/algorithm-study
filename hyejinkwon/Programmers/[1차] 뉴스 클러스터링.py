# 자카드 유사도 = 두 집합의 교집합 크기 // 두 집합의 합집합 크기
import math
from itertools import chain # 새로 알게된 라이브러리

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1_combi = []
    str2_combi = []
    
    str1_dict = {}
    str2_dict = {}
    
    intersect_set = 0
    union_set = 0
    
    for i1 in range(len(str1)-1) :
        s1 = str1[i1:i1+2]
        if s1.isalpha() :
            str1_combi.append(s1)
            
    for i2 in range(len(str2)-1) :
        s2 = str2[i2:i2+2]
        if s2.isalpha() :
            str2_combi.append(s2)
    
    for s1 in str1_combi :
        if s1 in str1_dict :
            str1_dict[s1] += 1
        else :
            str1_dict[s1] = 1
    
    for s2 in str2_combi :
        if s2 in str2_dict :
            str2_dict[s2] += 1
        else :
            str2_dict[s2] = 1
            
    str_dict = {}
    for key,value in chain(str1_dict.items(), str2_dict.items()) :
        if key in str_dict :
            str_dict[key].append(value)
        else :
            str_dict[key] = [value]
            
    for key,value_list in str_dict.items() :
        if len(value_list) >= 2 :
            union_set += max(value_list)
            intersect_set += min(value_list)
        elif len(value_list) == 1 :
            union_set += value_list[0]
    
    if union_set == 0 :
        return 65536
    else :
        answer = math.trunc(intersect_set/union_set*65536)
    
    return answer