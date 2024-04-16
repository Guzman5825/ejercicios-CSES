cantNumDiferentes=1
N= int(input())
vectorNum =list(map(int,input().split()))
vectorNum.sort()
 
numeroActual=vectorNum[0]
for i in range(N):
    if(vectorNum[i]!=numeroActual):
        cantNumDiferentes+=1
        numeroActual=vectorNum[i]
 
print(cantNumDiferentes)