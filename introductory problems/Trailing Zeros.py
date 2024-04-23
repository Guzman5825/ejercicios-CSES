#la solucion de este problema es econtrar los multiplos de 5,25(5^2),125(5^3)
#ya que siempre estos multiplos al multiplicar le daran un 0 extra al final
#no se usa factorial por que el coste N=10**9 es muy costoso (mas de 1 minuto)
N=int(input())
cantCeros=0

i=5

while i<=N:
    cantCeros+=N//i
    i*=5
print(cantCeros)
