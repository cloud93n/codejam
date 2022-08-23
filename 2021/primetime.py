import time,sys
start_time = time.time()

def inp():
    return int(input())

def inpli():
    return list(map(int, input().split()))

def inpls():
    return input().split()

def solve():
    M = inp()
    prime = []
    score = []
    for i in range(M):
        line = inpli()
        prime+=[line[0]]*line[1]
    print(prime)
   
    return 0 if len(score) == 0 else max(score)


T=inp()
for i in range(T):
    result = solve()
    print('Case #{}: {}'.format(i+1,result))

print('Time_elapsed :',time.time()-start_time,' s')