#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              reverse.py
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
#    Time:                   2021/10/04-2021/10/04 (1.0)
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
#     <abcd...> (abcd is integer)
#
# output:
#     <...dcba>
#

def reverse_print(n) :
    assert n>=0
    unit_digit = n%10
    left_number = n//10
    print(unit_digit, end="")
    if left_number>0 :
        reverse_print(left_number)
    else:
        print()

if __name__=="__main__" :
    number = int(input())
    reverse_print(number)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of reverse.py
#
#\*_________________________________________________________*/
