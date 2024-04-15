N=int(input())
vectorNum =list(map(int,input().split()))
numeros=[0]*(N+1)

for i in vectorNum:
    numeros[i]=1

numFaltante=1;
while numeros[numFaltante]!=0:
    numFaltante+=1
print(numFaltante)