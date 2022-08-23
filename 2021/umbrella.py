import time,sys
start_time = time.time()

def inp():
    return int(input())

def inpli():
    return list(map(int, input().split()))

def inpls():
    return input().split()

def solve(T):
    line=inpls()
    X=int(line[0])
    Y=int(line[1])
    S=line[2]
    tot_empty=S.count('?')
    poss = 2**tot_empty
    min_cost=0

    for i in range(poss):
        char_ls = ['C' if x=='0' else 'J' for x in '{:0{size}b}'.format(i,size=tot_empty)]
        replaced=list(S)
        char_idx=0
        for k in range(len(replaced)):
            if replaced[k]=='?':
                replaced[k] = char_ls[char_idx]
                char_idx+=1

        jc,cj=0,0
        for j in range(len(replaced)-1):
            
            if replaced[j]=='J' and replaced[j+1] == 'C':
                jc+=1
            elif replaced[j]=='C' and replaced[j+1] == 'J':
                cj+=1
    
        cost=cj*X+jc*Y

        if i==0:
            min_cost=cost
        else:
             if cost < min_cost: 
                 min_cost = cost

    print('Case #{}: {}'.format(T,min_cost))

T=inp()
for i in range(T):
   solve(i+1)

print('Time_elapsed :',time.time()-start_time,' s')