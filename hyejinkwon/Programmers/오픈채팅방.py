def solution(record):
    answer = []
    uid_in_out = []
    uid_name = {}
    
    for r in record :
        r_test = r.split()
        if r_test[0] == "Leave" :
            op,uid = r.split()
        else :
            op, uid, name = r.split()
        
        if op == "Enter" :
            uid_in_out.append([uid,1])
            uid_name[uid] = name
                
        elif op == "Leave" :
            uid_in_out.append([uid,0])
                
        elif op == "Change" : 
            uid_name[uid] = name
            
    for uid, op in uid_in_out :
        if op == 1 :
            answer.append(uid_name[uid]+"님이 들어왔습니다.")
        elif op == 0 :
            answer.append(uid_name[uid]+"님이 나갔습니다.")
            
    return answer