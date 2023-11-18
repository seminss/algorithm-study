# 10분
# T = int(input())
# for test_case in range(1, T + 1):
#     item_cnt = int(input())
#     data = []
#     for i in range(item_cnt):
#         ch, num = map(str, input().split())
#         data.extend(ch for _ in range(int(num)))
#
#     print(f"#{test_case}")
#     cnt = 0
#     while cnt < len(data):
#         for j in range(10):
#             if cnt >= len(data):
#                 break
#             print(data[cnt], end="")
#             cnt += 1
#         print()

T = int(input())
for test_case in range(1, T + 1):
    item_cnt = int(input())
    data = ""
    for i in range(item_cnt):
        ch, num = map(str, input().split())
        data += ch * int(num)
    print(f"#{test_case}")
    cnt = 0
    while cnt < len(data):
        print(data[cnt:cnt + 10])
        cnt += 10
