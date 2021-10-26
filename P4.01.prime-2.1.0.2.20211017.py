#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              prime-2.py
#
#    Version:                1.0
#
#    Build:                  2
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
#     2
#     3
#     5
#     7
#     ...
#     prime (<=n)
#

import math

def is_prime(number) :
    # assert n>=2
    square_root = int(math.sqrt(number))
    for divisor in range(2, square_root+1) :
        if number % divisor == 0 :
            return False
    return True

if __name__=="__main__" :
    max_number = int(input())+1
    for number in range(2, max_number) :
        if is_prime(number) :
            print(number)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of prime-2.py
#
#\*_________________________________________________________*/
