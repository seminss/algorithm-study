def solution(people, limit):
    answer = 0
    people.sort()
    i=0 #앞
    j=len(people)-1 #뒤
    while j>=i and len(people)!=0:
        if people[i]+people[j]<=limit:
            j-=1
            i+=1
        else:
            j-=1
        answer+=1
    return answer