#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              prime-5.py
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

primes = [2]
print(primes[0])

for number in range(3, max_number+1, 2) :
    is_prime = True
    square_root = math.sqrt(number)
    check_count = int(square_root/math.log(square_root)*1.3)
    if check_count > len(primes) :
        check_count = len(primes)

    for index in range(check_count) :
        if number%primes[index]==0 :
            is_prime = False
            break

    if is_prime :
        primes.append(number)
        print(number)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of prime-5.py
#
#\*_________________________________________________________*/
