MOD = 10**9 + 7  # Definición de la constante MOD

N=int(input())
dp=[0]*(N+1)   #vector que guardara el conjunto de soluciones

if N<=6:    # si son los primeros 6 numeros son calculables
    print(2**(N-1))
else:
    dp[0]=1     
    for i in range(1,7):
        dp[i]=2**(i-1)
    for i in range(7,N+1):
        dp[i]=(dp[i-1]*2-dp[i-7])%MOD
    print(dp[N])

