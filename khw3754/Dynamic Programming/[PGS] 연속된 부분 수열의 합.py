def solution(sequence, k):
    answer = []
    answer_len = len(sequence) + 1

    sta = 0
    end = 0
    sum = sequence[sta]

    while end != len(sequence) - 1 or sum >= k:
        if sum < k:
            if end == len(sequence) - 1:
                break
            end += 1
            sum += sequence[end]
        elif sum == k:
            if answer_len > end - sta + 1:
                answer = [sta, end]
                answer_len = end - sta + 1
            # print(sta, end, sum, answer_len,'&&&&&&&&')
            sum -= sequence[sta]
            sta += 1
        elif sum > k:
            sum -= sequence[sta]
            sta += 1

        # print(sta, end)

    return answer