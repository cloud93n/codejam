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
    N = inp()
    number = inpli()

    minop = 0
    for i in range(N-1):
        number1 = number[i]
        number2 = number[i+1]
        num1len = int(math.log10(number1))+1+minop
        num2len = int(math.log10(number2))+1

        if num1len > num2len:
            diff = num1len-num2len
            print(diff)

            if diff == 0:
                minop+=1
            else:
                minop+=diff

    return minop

T=inp()
for i in range(T):
    result = solve()
    print('Case #{}: {}'.format(i+1,result))

print('Time_elapsed :',time.time()-start_time,' s')