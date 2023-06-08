#12:22~ 12:49
from collections import Counter
def solution(topping):
    dic=Counter(topping)
    set_dic=set()
    answer=0
    for i in topping:
        dic[i]-=1
        set_dic.add(i)
        if dic[i]==0:
            dic.pop(i)
        if len(dic)==len(set_dic):
            answer+=1
    return answer

# 처음에는 슬라이싱하고 set과 Counter로 묶는 방법으로 풀었었는데,, 올바른 사용법이 아니였다.(시간초과)
# 딕셔너리로 조회를 하게 되면 갯수 조회가 상당히 빨라지기 때문에 Counter로 갯수를 저장해두고,
# key를 한 번씩 사용할 때마다 value에 저장된 count를 줄여주면 된다. 매우 빠른 조회가 가능하다!!