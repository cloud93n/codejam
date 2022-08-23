import time,sys
start_time = time.time()

from itertools import permutations


def inp():
    return int(input())

def inpli():
    return list(map(int, input().split()))

def inpls():
    return input().split()

def calculate_cost(N,tup):
    cost=0
    L=list(tup)
    for i in range(N-1):
        min_val = min(L[i:N])
        j = L.index(min_val)
        L[i:j+1]=L[i:j+1][::-1]
        cost+=j-i+1
    return cost

def solve(T):
    line = inpli()
    N = line[0]
    C = line[1]

    # if C < N or C > 2*N-2:
    #     return 'IMPOSSIBLE'
    number = range(1,N+1)
    for i in permutations(number,N):
        cost = calculate_cost(N,i)
        if cost == C:
            return " ".join([str(x) for x in i])


    return 'IMPOSSIBLE'


T=inp()
for i in range(T):
    result = solve(i+1)
    print('Case #{}: {}'.format(i+1,result))

print('Time_elapsed :',time.time()-start_time,' s')