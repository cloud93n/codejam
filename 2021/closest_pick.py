import time,sys
start_time = time.time()

import math

def inp():
    return int(input())

def inpli():
    return list(map(int, input().split()))

def inpls():
    return input().split()

def solve():
    line1 = inpli()
    line2 = inpli()
    N = line1[0]
    K = line1[1]

    num_list = list(range(1,K+1))
    can_buy = list(set(num_list) - set(line2))
    print(can_buy)
    bin_list = [0]*K
    max_prob = 0
    can_buy_len = len(can_buy)
    if can_buy_len <= 2:
        max_prob = can_buy_len/K
    else:
        for c in line2:
            bin_list[c-1] = 1 

        bin_str = "".join(map(str, bin_list))
        zeroone = bin_str.count('01')
        onezero = bin_str.count('10')
        if bin_list[-1]==1:
            max_prob = (K-(zeroone+onezero+1))/K
        else:
            max_prob = (K-(zeroone+onezero))/K


        print(bin_str)
        print(zeroone)
        print(onezero)

    # print(max_prob)


    return max_prob

T=inp()
for i in range(T):
    result = solve()
    print('Case #{}: {}'.format(i+1,result))

print('Time_elapsed :',time.time()-start_time,' s')