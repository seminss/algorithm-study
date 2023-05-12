import sys

n=int(sys.stdin.readline())
arr=list(sys.stdin.readline().strip())
values={} # 각 알파벳에 해당하는 실제 값을 저장할 딕셔너리

# 처음에는 여기서 dictionary 를 사용하지 않고 replace 하는 식으로 알파벳 -> 숫자 변환을 했는데
# 그러면 숫자가 바뀔 때마다 인덱스 문제가 생긴다.
for i in range(n):
    x=sys.stdin.readline().strip()
    values[chr(65+i)]=float(x)

num_list=[]

for ch in arr:
    if ch.isalpha():
        num_list.append(values[ch])
    else:
        num1=num_list.pop()
        num2=num_list.pop()
        if ch=='+':
            num_list.append(num2+num1)
        elif ch=='-':
            num_list.append(num2-num1)
        elif ch=='*':
            num_list.append(num2*num1)
        elif ch=='/':
            num_list.append(num2/num1)
    
print("{:.2f}".format(num_list[0]))