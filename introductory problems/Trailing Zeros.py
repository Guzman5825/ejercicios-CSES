#

N=int(input())
cantCeros=0

i=5

while i<=N:
    cantCeros+=N//i
    i*=5
print(cantCeros)