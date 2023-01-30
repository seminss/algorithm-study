n=int(input())
word_list=[0 for i in range(n)]
for i in range(n):
    word_list[i]=input()

word_list=list(set(word_list)) #중복 제거
word_list.sort(key=len) #길이순 정렬

pair_list=[]
for i in word_list:
    pair_list.append((len(i),i))

result_list=sorted(pair_list)
for l,w in result_list:
    print(w)