import sys

m=int(sys.stdin.readline())
S=set() #전역

for i in range(m):
    cmd=sys.stdin.readline()

    if "add" in cmd:
        a,x=map(str,cmd.split())
        S.add(int(x))

    elif "remove" in cmd:
        r,x=map(str,cmd.split())
        S.discard(int(x))

    elif "check" in cmd:
        c,x=map(str,cmd.split())
        if int(x) in S:
            print(1)
        else:
            print(0)

    elif "toggle" in cmd:
        t,x=map(str,cmd.split())
        if int(x) in S:
            S.remove(int(x))
        else:
            S.add(int(x))

    elif "all" in cmd:
        S=set(j for j in range(1,21))

    elif "empty" in cmd:
        S.clear()