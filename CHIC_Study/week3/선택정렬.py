array=[7,5,9,0,3,1,6,2,4,5]

for i in range(len(array)):
    min_index=i #가장 작은 원소의 인덱스
    for j in range(i+1,len(array)):
        if array[min_index]>array[j]:
            min_index=j #더 작은 원소가 있으면 인덱스 갱신
    array[i], array[min_index]=array[min_index],array[i] #swap

print(array)