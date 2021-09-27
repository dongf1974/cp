#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              factorial.py
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
#    Time:                   2021/09/15-2021/09/27 (1.0)
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
#     n!
#
# note:
#     n! = n * (n-1) * ... * 1
#

def factorial(n) :
    assert n>=0
    if n==0 :
        return 1
    else :
        return n * factorial(n-1)

if __name__=="__main__" :
    number = int(input())
    factorial_value = factorial(number)
    print(factorial_value)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of factorial.py
#
#\*_________________________________________________________*/
