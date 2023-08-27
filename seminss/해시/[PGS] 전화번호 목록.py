def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if len(phone_book[i])<=len(phone_book[i+1]):
            if phone_book[i+1][:len(phone_book[i])]==phone_book[i]:
                return False
    return True

# 처음에는 sort를 길이 순서대로 정렬해서 비교하는 것으로 생각했다. -> 효율성 2개 out
# key값을 따로 주지 않은 채 sort()를 쓰게 되면 
# "123", "12348", "1235" 와 같이 접두어인 경우 이웃하게 위치하게 되어 시간 복잡도가 훨씬 줄어든다.