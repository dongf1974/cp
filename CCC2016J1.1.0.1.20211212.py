#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    File Name:              CCC2016J1.py
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
#    Time:                   2021/12/12-2021/12/12 (1.0)
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
# CCC 2016 Problem J1: Tournament Selection
# http://cemc.uwaterloo.ca/contests/computing/2016/index.html
#

win = 0
for game in range(6) :
	result = input()
	assert result=='W' or result=='L'
	if result=='W' :
		win += 1
assert win>=0
assert win<=6

if win>=5 :
	group = 1
elif win>=3 :
	group = 2
elif win>=1 :
	group = 3
else :
	group = -1

print(group)

#/*~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~*\
#
#    End of CCC2016J1.py
#
#\*_________________________________________________________*/
