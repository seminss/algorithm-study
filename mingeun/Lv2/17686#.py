''' 2023.5.23
19:50 ~ 20:28
'''

def split_filename(file):
    n_index = 0
    while not str.isdigit(file[n_index]):
        n_index += 1
    t_index = n_index
    while t_index < len(file) and str.isdigit(file[t_index]):
        t_index += 1
    return file[:n_index], file[n_index:t_index], file[t_index:]
    
    
def solution(files):
    '''
    100자 이내, 영문 대소문자, 숫자, 공백, 마침표, 빼기 부호
    HEAD 한 자 이상의 문자열
    NUMBER 1~5자리 숫자
    TAIL
    '''
    # ORIGINAL: 원래 순서 보존
    HEAD, NUMBER, TAIL, ORIGINAL = 0, 1, 2, 3
    tmp = [ split_filename(file) + tuple([i]) for i, file in enumerate(files) ]
    tmp.sort(key=lambda x: (x[HEAD].lower(), int(x[NUMBER]), x[ORIGINAL]))
    answer = [ f[HEAD] + f[NUMBER] + f[TAIL] for f in tmp ]
    return answer
