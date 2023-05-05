T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    arr = [i for i in range(m+1)]
    for _ in range(n-1):
        new_arr = []
        for i in range(len(arr)):
            new_arr.append(sum(arr[:i+1]))
        arr = new_arr
    print(arr[m-n+1])