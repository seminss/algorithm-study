'''
장르별 가장 많이 재생된 노래 2개씩

4 : pop : 2500
3 : classic : 800
1 : pop : 600 
0 : classic : 500
2 : classic : 150
'''

def solution(genres, plays):
    answer = []
    genres_dict = {}
    genres_count_dict = {}
    
    for i in range(len(genres)) :
        if genres[i] in genres_dict :
            genres_dict[genres[i]].append([plays[i], i])
        else :
            genres_dict[genres[i]] = [[plays[i], i]]
            
        if genres[i] in genres_count_dict :
            genres_count_dict[genres[i]] += plays[i]
        else :
            genres_count_dict[genres[i]] = plays[i]
    
    for key, value in sorted(genres_count_dict.items(), key= lambda x : x[1], reverse=True) :
        index_count = 0
        for count, index in sorted(genres_dict[key], key=lambda x : (x[0],-x[1]), reverse=True) :
            if index_count == 2 :
                continue
            
            if len(genres_dict[key]) == 1 : answer.append(index)
            else :
                index_count += 1
                answer.append(index)
    
    return answer