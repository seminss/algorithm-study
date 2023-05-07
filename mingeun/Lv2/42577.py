''' 2023.5.7 
16:28 ~ 16:37
'''
def solution(phone_book):
    # 전화번호를 길이에 대한 오름차순 정렬
    phone_book.sort(key=lambda x: len(x))
    bucket = dict()
    for number in phone_book:
        k = '' 
        for n in number:
            k += n
            if k in bucket:
                return False
        bucket[number] = 1
    return True
