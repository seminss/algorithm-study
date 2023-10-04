N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def dfs(nums, list):
    if len(list) == M:
        print(*list)
        return

    for i in range(len(nums)):
        copiedList = list[::]
        copiedNums = nums[::]
        # copiedNums.pop(i)
        copiedList.append(nums[i])
        dfs(copiedNums, copiedList)

dfs(nums, [])