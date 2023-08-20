import heapq


def solution(scovil, K):
    answer = 0

    heapq.heapify(scovil)
    while scovil[0] < K and len(scovil) > 1:
        mix = heapq.heappop(scovil) + heapq.heappop(scovil) * 2
        heapq.heappush(scovil, mix)
        answer += 1

    if len(scovil) == 1 and scovil[0] < K:
        return -1

    return answer