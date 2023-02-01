n1=n2=int(input())
result=0

if n1>=5:
    if n1%5==0:
        result=n1//5
    for i in range(1,n1//5+1):
        if (n1-i*5)%3==0:
            result=i+(n1-i*5)//3
    if result!=0:
        print(result)
        exit()
if n2>=3:
    if n2%3==0:
        result=n2//3
    for i in range(1,n2//3+1):
        if (n2-i*3)%5==0:
            result=i+(n2-i*3)//5
    if result!=0:
        print(result)
        exit()
    
print(-1)
