n = int(input())
nums = list(map(int, input().split()))


max = 0
pre_sum = 0
last = 0
for num in nums:
    if num > last:
        pre_sum += num
    else:
        if pre_sum > max:
            max = pre_sum
        pre_sum = 0
    last = num
print(max)