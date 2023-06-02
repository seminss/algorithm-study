# def solution(numbers):
#     answer = [-1]*len(numbers)
#     for i,n in enumerate(numbers):
#         for e in numbers[i:]:
#             if n<e:
#                 answer[i]=e
#                 break
#     return answer
