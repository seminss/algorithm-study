T = int(input())

def findIndex(list, n, limit):
    for i in range(len(list) - 1, limit, -1):
        if list[i] == n:
            return i
    return -1

prices = []
for i in range(T):
    result = 0
    N = int(input())
    prices = list(map(int, input().split()))

    ### 내가 푼거 (런타임 에러)
    # sortedPrices = sorted(prices, key=lambda x: -x)
    #
    # # 처리한 것
    # # checkedIndex = [False for _ in range(N)]
    # lastSold = -1
    #
    # for price in sortedPrices:
    #     index = findIndex(prices, price, lastSold)
    #     if index != -1 and index > lastSold:
    #         result += (index - lastSold - 1) * prices[index] - sum(prices[lastSold+1:index])
    #         # checkedIndex.append(index)
    #         lastSold = index

    ### 두번째 방법 (정답)
    maxPrice = 0
    for index in range(N - 1, -1, -1):
        if prices[index] > maxPrice:
            maxPrice = prices[index]
        else:
            result += maxPrice - prices[index]

    print('#' + str(i+1) + ' ' + str(result))