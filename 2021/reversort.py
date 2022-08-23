import time
start_time = time.time()

def inp():
    return int(input())

def inpli():
    return list(map(int, input().split()))

def inpls():
    return input().split()

def solve(T):
    N=inp()
    L=inpli()
    cost=0
    for i in range(N-1):
        min_val = min(L[i:N])
        j = L.index(min_val)
        L[i:j+1]=L[i:j+1][::-1]
        cost+=j-i+1
    print('Case #{}: {}'.format(T,cost))

T=inp()
for i in range(T):
   solve(i+1)

print('Time_elapsed :',time.time()-start_time,' s')