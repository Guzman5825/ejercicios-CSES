N = int (input())
while N != 1:
    print(f"{N}",end=" ")
    if N%2==0:
        N=int(N/2)
    else:
        N=int(N*3+1)
print(N)