N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def dfs(nums, list):
    if len(list) == M:
        print(*list)
        return

    last = -1
    for i in range(len(nums)):
        if last == nums[i]:
            continue
        last = nums[i]
        copiedNums = nums[i::]
        copiedList = list[::]
        copiedList.append(copiedNums.pop(0))
        dfs(copiedNums, copiedList)

dfs(nums, [])
