N = int(input())
nums = list(map(int, input().split()))
counts = list(map(int, input().split()))
def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def prod(a, b):
    return a * b
def sub(a, b):
    if a >= 0:
        return a // b
    else:
        return -(-a // b)
operators = [plus, minus, prod, sub]

max = None
min = None
def dfs(nums, counts):
    global max, min
    if len(nums) == 2:
        result = operators[counts.index(1)](nums[0], nums[1])
        if max == None or max < result:
            max = result
        if min == None or min > result:
            min = result
        return

    for i in range(4):
        if counts[i] > 0:
            copiedNums = nums[::]
            nums[1] = operators[i](nums[0], nums[1])
            nums = nums[1:]
            counts[i] -= 1
            dfs(nums, counts)
            # backtrack
            nums = copiedNums
            counts[i] += 1


dfs(nums, counts)
print(max, min)