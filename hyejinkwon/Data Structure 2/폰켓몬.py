def solution(nums):
    answer = 0 
    phone_ketmon = dict()
    get_n = len(nums)//2
    
    for n in nums :
        if n in phone_ketmon : phone_ketmon[n] += 1
        else : phone_ketmon[n] = 1
    
    phone_ketmon = sorted(phone_ketmon.items(), key = lambda x : x[1])
    phone_ketmon_list = []
    
    for key, value in phone_ketmon :
        phone_ketmon_list.append([key, value])
        
    phone_n = len(phone_ketmon_list)
    answer_set = set()
    i = 0
    
    while get_n > 0 :
        if phone_ketmon_list[i%phone_n][1] > 0 :
            phone_ketmon_list[i%phone_n][1] -= 1
            answer_set.add(phone_ketmon_list[i%phone_n][0])
            get_n -= 1
        i += 1
        
    answer = len(answer_set)
    
    return answer