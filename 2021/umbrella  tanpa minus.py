import time,sys
start_time = time.time()

def inp():
    return int(input())

def inpli():
    return list(map(int, input().split()))

def inpls():
    return input().split()

def fill_empty(i,X,Y,mural):
    if mural[i]=='J' and mural[i+1]=='?':
        mural[i+1]='J'
    elif mural[i]=='C' and mural[i+1]=='?':
        mural[i+1]='C'

def solve(T):
    line=inpls()
    X=int(line[0])
    Y=int(line[1])
    S=line[2]

    min_cost=0
    replaced=list(S)

    replaced_c=S.replace('C','J')
    start_idx = replaced_c.find('J')

    if start_idx==-1: 
       return 0

    for i in range(start_idx,len(replaced)-1):
        fill_empty(i,X,Y,replaced)

    if start_idx>=0:
        reversed_start=replaced[:start_idx+1][::-1]
        for i in range(start_idx):
            fill_empty(i,X,Y,reversed_start)

        replaced[:start_idx+1]=reversed_start

    jc,cj=0,0
    for j in range(len(replaced)-1):
        
        if replaced[j]=='J' and replaced[j+1] == 'C':
            jc+=1
        elif replaced[j]=='C' and replaced[j+1] == 'J':
            cj+=1

    min_cost=cj*X+jc*Y

    return min_cost


T=inp()
for i in range(T):
    result = solve(i+1)
    print('Case #{}: {}'.format(i+1,result))

print('Time_elapsed :',time.time()-start_time,' s')