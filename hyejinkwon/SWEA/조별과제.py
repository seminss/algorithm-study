TC = int(input())

for test_case in range(1, TC + 1):
    N = int(input())
    number = list(map(int, input().split()))
    answer = 0

    for i in range(1,N-1) :
        min_value = min([number[i-1], number[i], number[i+1]])
        max_value = max([number[i-1], number[i], number[i+1]])
        if number[i] != min_value and number[i] != max_value :
            answer += 1

    print("#%d %s" %(test_case, answer))
