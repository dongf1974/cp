#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              triangle3.a3.py
#
#    Version:                1.2
#
#    Build:                  4
#
#    Author:                 Dong Fang (Walter Dong)
#
#    Contact:                dongfang@ustc.edu
#                            dongf@live.com
#
#    Time:                   2021/08/12-2021/08/12 (1.0)
#                            2021/08/12-2021/08/12 (1.1)
#                            2021/08/12-2021/08/12 (1.2)
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
#     <line count>
#
# output:
#          *
#         ***
#         ...
#     **...*...**
#

def print_character(character, count) :
	for column in range(count) :
		print(character, end="")

line_count = int(input())
for line in range(line_count) :
	print_character(" ", line_count-(line+1))
	print_character("*", line*2+1)
	print()

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of triangle3.a3.py
#
#\*_________________________________________________________*/
