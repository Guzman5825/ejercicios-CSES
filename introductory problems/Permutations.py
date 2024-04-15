N=int(input())

if N!=2 and N!=3 :
    i=2
    while i<=N:
        print(i,end=" ")
        i+=2
    i=1
    while i<=N:
        print(i,end=" ")
        i+=2
else:
    print("NO SOLUTION")