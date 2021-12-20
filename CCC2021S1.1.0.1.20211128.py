#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              CCC2021S1.py
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
#    Time:                   2021/11/28-2021/11/28 (1.0)
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
# CCC 2021 Problem S1: Crazy Fencing
# http://cemc.uwaterloo.ca/contests/computing/2021/index.html
#

fence_count = int(input())
heights = list(map(int, input().split()))
widths = list(map(int, input().split()))
assert len(heights)==fence_count+1
assert len(widths)==fence_count

area_2 = 0
for index in range(fence_count) :
	height_1 = heights[index]
	height_2 = heights[index+1]
	width = widths[index]
	area_2 += (height_1+height_2)*width

if area_2%2==0 :
	area = int(area_2/2)
else :
	area = area_2/2
print(area)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of CCC2021S1.py
#
#\*_________________________________________________________*/
