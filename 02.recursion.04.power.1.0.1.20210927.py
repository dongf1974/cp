#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              power.py
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
#    Time:                   2021/09/27-2021/09/27 (1.0)
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
#     <a, n>
#
# output:
#     power(a, n) = a^n
#

def power(a, n) :
    assert a>0
    assert n>=0
    if n==0 :
        return 1
    else :
        assert n>=1
        half_power = power(a, int(n/2))
        result = half_power*half_power
        if n%2==1 :
            result *= a
        return result

if __name__=="__main__" :
    a = int(input())
    n = int(input())
    power_value = power(a, n)
    print(power_value)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of gcd.py
#
#\*_________________________________________________________*/
