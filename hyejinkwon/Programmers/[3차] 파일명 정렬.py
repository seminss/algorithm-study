def solution(files):
    answer = []
    sort_result = []
    
    for f in files :
        head,number,tail = "","",""
        for index, w in enumerate(f) :
            if w.isdigit() :
                head = f[:index]
                number = f[index:]
                
                for index, n in enumerate(number) :
                    if not n.isdigit():
                        tail = number[index:]
                        number = number[:index]
                        break    
                
                sort_result.append([head,number,tail])
                head,number,tail = "","",""
                break
                
        sort_result = sorted(sort_result, key = lambda x : (x[0].lower(), int(x[1])))
                
    for s in sort_result :
        answer.append("".join(s))
    
    return answer