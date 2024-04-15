N=int(input())
numeros=list(map(int,input().split()))
cantMovimientos=0

for i in range(0,N-1):
    if numeros[i]>numeros[i+1]:
        cantMovimientos+=numeros[i]-numeros[i+1]
        numeros[i+1]=numeros[i]

print(cantMovimientos)

