T = int(input())

possible = set()

for i in range(1,10) :
    for j in range(1,10) :
        possible.add(i*j)

for test_case in range(1, T + 1) :
    number = int(input())
    if number in possible :
        answer = "Yes"
    else :
        answer = "No"
    
    print("#%d %d" %(test_case, answer))
