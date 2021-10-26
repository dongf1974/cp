#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              prime-1.py
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

def is_prime(number) :
    # assert n>=2
    for divisor in range(2, number) :
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
#    End of prime-1.py
#
#\*_________________________________________________________*/
