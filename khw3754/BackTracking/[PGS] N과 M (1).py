N, M = map(int, input().split())

nums = [i for i in range(1, N+1)]

def dfs(nums, list):
    if len(list) == M:
        print(*list)
        return

    for i in range(len(nums)):
        copiedList = list[::]
        copiedNums = nums[::]
        n = copiedNums.pop(i)
        copiedList.append(n)
        dfs(copiedNums, copiedList)

dfs(nums, [])




# def dfs(nums, list):
#     if len(list) == M:
#         print(*list)
#         return
#
#     print('dd')
#
#     for i in range(len(nums)):
#         copiedList = list[::]
#         n = nums[i]
#         # nums = nums[:i] + nums[i+1:]
#         nums.remove(n)
#
#         copiedList.append(n)
#         dfs(nums, copiedList)
#         nums = nums[:i] + [n] + nums[i:]        ############### 얘가 문제. 원본이랑 다른 객체가 돼버림
#         # nums.insert(i, n)
#
#
#     print('dd')
#
# N, M = map(int, input().split())
#
# nums = [i for i in range(1, N+1)]
#
# dfs(nums, [])
