N, X = map(int, input().split())
hits = list(map(int, input().split()))

max_sum = sum(hits[:X])
pre_sum = max_sum
count = 1
sta = 0
end = X-1

for _ in range(N - X):
    pre_sum = pre_sum - hits[sta] + hits[end + 1]
    end += 1
    sta += 1

    if pre_sum > max_sum:
        max_sum = pre_sum
        count = 1
    elif pre_sum == max_sum:
        count += 1

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(count)