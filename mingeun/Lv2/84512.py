''' 2023.5.20
17:10 ~ 17:38
'''
def create_dictionary(arr, alphabets, l, dictionary):
    """
    AEIOU를 사용하여 만들 수 있는 길이 5 이하의 모든 문자열 생성
    6^5 - 1 개의 문자열이 생성된다
    """
    if len(arr) == l:
        return
    else:
        for c in alphabets:
            arr.append(c)
            # print(arr)
            dictionary.append(''.join(arr))
            create_dictionary(arr, alphabets, l, dictionary)
            arr.pop()
        
        
def solution(word):
    answer = 0
    dictionary = []
    create_dictionary([], ['A', 'E', 'I', 'O', 'U'], 5, dictionary)
    while answer < len(dictionary):
        if dictionary[answer] == word:
            return answer + 1
        else:
            answer += 1
    return -1
