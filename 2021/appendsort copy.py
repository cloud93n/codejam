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
        number1=number[i]
        number2 = number[i+1]
        num1len = int(math.log10(number1))+1
        num2len = int(math.log10(number2))+1
        diff = num1len-num2len
        digit_list2 = str(number2)

        if number1>= number2:
            if num1len>num2len:
                digit2_0str = digit_list2+'0'*(diff)
                digit2_0int = int("".join(map(str, digit2_0str)))

                digit2_9str = digit_list2+'9'*(diff)
                digit2_9int = int("".join(map(str, digit2_9str)))
                if digit2_0int > number1:
                    minop+=diff
                    number[i+1] = digit2_0int
                elif digit2_0int <= number1 and digit2_9int > number1:
                    minop+=diff
                    number[i+1] = number1+1
                else:
                    minop+=diff+1
                    digit2_0str = digit_list2+'0'*(diff)+'0'
                    number[i+1] =  int("".join(map(str, digit2_0str)))
            else:
                digit_list2 +'0'
                minop+=1
                number[i+1]= int("".join(map(str, digit_list2)))

    return minop


T=inp()
for i in range(T):
    result = solve()
    print('Case #{}: {}'.format(i+1,result))

print('Time_elapsed :',time.time()-start_time,' s')