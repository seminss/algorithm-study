def dfs(result):
    if len(result) == M:
        print(*result)
    else:
        for i in range(len(nums)):
            tmp = nums[i]
            result.append(tmp)
            nums.pop(i)

            dfs(result.copy())

            result.pop()
            nums.insert(i, tmp)


N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

r = []
dfs(r)

