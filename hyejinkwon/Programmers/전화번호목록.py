# 접두어 있는지 확인

def solution(phone_book):
    answer = True
    phone_hash = {}
    for p in phone_book :
        phone_hash[p] = 1
        
    for p in phone_book:
        word = ""
        for p_i in p :
            word += p_i
            if word in phone_hash and word != p :
                return False
    return True
    
    return answer