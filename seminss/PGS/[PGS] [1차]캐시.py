# LRU : 가장 오랫동안 참조되지 않은 페이지를 교체하는 알고리즘
# 캐시에 있는지 없는지, 없다면 새로 넣어야 하는데 캐시가 꽉찼는지 안찼는지
# cache hit : 캐시에 있는 도시를 참조, 해당 도시가 캐시 내에서 맨 앞으로 이동
# cache miss : 캐시에 없는 도시를 참조, 캐시에 새로 들어감, 가장 old 한 건 삭제

def solution(cacheSize, cities):
    answer = 0
    cache=[] #최근에 들어온게 뒤, 오래된 게 맨 앞
    if cacheSize==0:
        return len(cities)*5 # 모든 경우가 cache miss
    for c in cities:
        c=c.lower()
        if c in cache: #cache hit
            answer+=1
            cache.remove(c)
            cache.append(c)
        else:
            if len(cache)==cacheSize:
                cache.pop(0)
            cache.append(c)
            answer+=5
    return answer


# cacheSize=0, cities=["LA","LA"] 인 경우 6이 아니라 10이 되어야 하는 경우를 고려
# 즉 모든 경우가 cache miss 인 경우 예외처리를 해주어야 한다.