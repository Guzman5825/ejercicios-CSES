def esDeptDeseado(a,b,k):
    if a>=b-k and a<=b+k:
        return True
    return False

N, M, K = map(int, input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A.sort()
B.sort()

cantDeptContratados=0
apliActual=0
deptActual=0


while apliActual<N and deptActual<M:
    if esDeptDeseado(A[apliActual],B[deptActual],K):
        cantDeptContratados+=1
        apliActual+=1
        deptActual+=1
    else:
        if A[apliActual]<(B[deptActual]-K):
            apliActual+=1
        else:
            deptActual+=1
print(cantDeptContratados)