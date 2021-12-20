#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              fibonacci-2.py
#
#    Version:                1.0
#
#    Build:                  1
#
#    Author:                 Dong Fang (Walter Dong)
#
#    Contact:                dongfang@ustc.edu
#                            dongf@live.com
#
#    Time:                   2021/10/17-2021/10/17 (1.0)
#
#    Notice:
#    Copyright (C) 2021, Dong Fang (Walter Dong).
#    All rights reserved.
#
#    This software is PROPRIETARY and CONFIDENTIAL. To get license,
#    contact Dong Fang (Walter Dong).
#-
#\*_________________________________________________________*/

#
# input:
#     <n>
#
# output:
#     fibonacci(n)
#
# note:
#     fibonacci(0) = 0
#     fibonacci(1) = 1
#     fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
#

def fibonacci(n) :
    assert n>=0
    if n<=1 :
        if n==0 :
            return 0
        else :
            assert n==1
            return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci_sequence = [0, 1]

number = int(input())

for index in range(2, number+1, 1) :
    fibonacci_value = fibonacci_sequence[index-1]+fibonacci_sequence[index-2]
    fibonacci_sequence.append(fibonacci_value)

print(fibonacci_sequence[number])

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of fibonacci-2.py
#
#\*_________________________________________________________*/
