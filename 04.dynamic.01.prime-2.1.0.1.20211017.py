#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              prime-2.py
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
#     2
#     3
#     5
#     7
#     ...
#     prime (<=n)
#

import math

max_number = int(input())

for number in range(2, max_number+1) :
    is_prime = True
    square_root = int(math.sqrt(number))

    for divisor in range(2, square_root+1) :
        if number%divisor==0 :
            is_prime = False
            break

    if is_prime :
        print(number)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of prime-2.py
#
#\*_________________________________________________________*/
