from collections import deque


def solution(cacheSize, cities):
    time = 0
    cache = deque()

    for city in cities:
        # 모두 소문자로 처리
        city = city.lower()
        # 캐시에 있다면 시간이 1만큼 걸림
        if city in cache:
            #### 문제: 캐시 순서를 바꿔줘야 함
            cache.remove(city)
            cache.append(city)
            time += 1
        # 캐시에 없으면 처리를 해주고 시간이 5걸림
        else:
            if cacheSize != 0:
                if len(cache) == cacheSize:
                    cache.popleft()
                cache.append(city)
            time += 5

    return time