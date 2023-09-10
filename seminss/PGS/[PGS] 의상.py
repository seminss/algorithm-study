# 답지 참고

#굳이 옷 종류를 dictionary로 만들지 않고, type에 해당하는 옷 개수만 저장해주면 된다.
def solution(clothes):
    hash_map={}
    for clothes, type in clothes:
        hash_map[type]=hash_map.get(type,0)+1 #hash_map에서 type에 해당하는 value 값을 가져오고, 없으면 0 할당
    answer=1
    for type in hash_map: #여기서 의상 가짓수별로 조합을 구하지 않고, 입은 경우, 안입은 경우를 같이 고려하면 자동으로 모든 경우가 세진다.
        answer*=(hash_map[type]+1)
    return answer-1 #아무것도 입지 않은 경우 -1