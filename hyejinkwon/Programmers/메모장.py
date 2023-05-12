# 다음과 같이 import를 사용할 수 있습니다.
# import math

# 영어단어는 정해진 순서대로
# 단어사이는 공백하나로 구분
# 한줄끝에 단어 하나 다 못적었으면 나머지부분 모두 공백, 다음줄부터 다시 단어시작


def solution(K, words):
    # 여기에 코드를 작성해주세요.
    answer = 0
    result = ""
    i = 0
    while i < len(words) :
        range_length = K - len(result)
        if len(words[i]) <= range_length :
            result += words[i]+"_"
        else :
            result = ""
            answer += 1
            i -= 1
            
        i+=1
    
    if result != "":
        answer += 1
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
K = 10
words = ["nice", "happy", "hello", "world", "hi"]
ret = solution(10, words)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")