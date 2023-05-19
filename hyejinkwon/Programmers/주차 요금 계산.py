def solution(fees, records):
    answer = []
    car = {}
    calculate_car = {}
    
    for r in records :
        time, number, option = r.split()
        h,m = time.split(":")
        
        if option == "IN" :
            car[number] = int(h)*60+int(m)
            
        elif option == "OUT" :
            try :
                calculate_car[number] += (int(h)*60+int(m)) - car[number]
            except :
                calculate_car[number] = (int(h)*60+int(m)) - car[number]
            del car[number]
            
    for number, time in car.items() :
        try :
            calculate_car[number] += (23*60+59) - time
        except :
            calculate_car[number] = (23*60+59) - time
    
    sorted_list = sorted(calculate_car.items(), key=lambda x : x[0])
        
    for number, time in sorted_list:
        print(number, time)
        money = fees[1]
        if time >= fees[0] :
            if (time-fees[0])%fees[2] == 0 : #나누어떨어진다면
                money += (time-fees[0])//fees[2]*fees[3]
            else : # 나누어 떨어지지 않는다면
                money += ((time-fees[0])//fees[2]+1)*fees[3]
            
        answer.append(money)
    
    return answer